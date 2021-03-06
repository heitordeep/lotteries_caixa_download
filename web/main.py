from datetime import datetime as dt
from os import path, system

from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_parameter
from pandas import read_csv

from db.connection import Database
from log_generator import RegisterLogs

app_web = Blueprint(
    'app_web', __name__, url_prefix='/web/', template_folder='templates'
)

prize_allowed = ['megasena', 'lotofacil', 'quina']
now = dt.now().strftime('%Y-%m-%d')

db = Database()
logger = RegisterLogs()


@app_web.route('/')
def index():
    return render_template('lotteries_caixa/index.html')


@app_web.route('/result/<prize>/')
def view(prize):

    if prize in prize_allowed and path.exists(
        f'lake/{prize}/{now}/tratado.csv'
    ):

        PAGE_SIZE = 250
        csv = read_csv(f'lake/{prize}/{now}/tratado.csv')

        csv.sort_values(by=['concurso'], inplace=True, ascending=False)

        csv = csv[csv['cidade'].notna()]
        csv = csv[csv['uf'].notna()]

        page = request.args.get(get_page_parameter(), type=int, default=1)

        row_data = csv[
            (page - 1) * PAGE_SIZE : page * PAGE_SIZE
        ].values.tolist()

        pagination = Pagination(
            page=page,
            total=len(csv),
            per_page=PAGE_SIZE,
            css_framework='bootstrap4',
        )

        return render_template(
            'lotteries_caixa/view.html',
            title=prize,
            headers=csv.columns.values,
            row_data=row_data,
            pagination=pagination,
        )
    return render_template(
        'lotteries_caixa/index.html',
        message=f'Not Found {prize.upper()} element!'
        f' Click in the button "Atualizar Dados"',
        color='danger',
    )


@app_web.route('/update/all/')
def update_csv():

    for prize in prize_allowed:
        system(f'python download.py {prize}')

        logger.debug_register(f'Successfully created {prize} file!')

        logger.debug_register(
            f'Reading lake/{prize}/{now}/tratado.csv file...'
        )
        csv = read_csv(f'lake/{prize}/{now}/tratado.csv')
        csv = csv.astype(str)  # Transform rows on string.

        payload = csv.to_dict('records')

        db.drop(prize)  # Drop prize collection.
        db.insert(prize, payload)

        logger.debug_register(f'{prize} saved successfully.')

    return render_template(
        'lotteries_caixa/index.html',
        message='Dados atualizados com sucesso',
        color='success',
    )
