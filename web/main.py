from datetime import datetime as dt
from os import path, system

from flask import Blueprint, render_template, request

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload
from db.connection import Database
from flask_paginate import Pagination, get_page_parameter
from log_generator import RegisterLogs
from pandas import read_csv

app_web = Blueprint(
    'app_web', __name__, url_prefix='/web/', template_folder='templates'
)

premium_allowed = ['megasena', 'lotofacil', 'quina']
now = dt.now().strftime('%Y-%m-%d')

db = Database()
logger = RegisterLogs()


@app_web.route('/')
def index():
    return render_template('lotteries_caixa/index.html')


@app_web.route('/result/<premium>/')
def view(premium):

    if premium in premium_allowed and path.exists(
        f'lake/{premium}/{now}/tratado.csv'
    ):

        PAGE_SIZE = 250
        csv = read_csv(f'lake/{premium}/{now}/tratado.csv')

        csv.sort_values(by=['Concurso'], inplace=True, ascending=False)

        csv = csv[csv['Cidade'].notna()]
        csv = csv[csv['UF'].notna()]

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
            title=premium,
            headers=csv.columns.values,
            row_data=row_data,
            pagination=pagination,
        )
    return render_template(
        'lotteries_caixa/index.html',
        message=f'Not Found {premium.upper()} element!'
        f' Click in the button "Atualizar Dados"',
        color='danger',
    )


@app_web.route('/update/')
def update_csv():

    list_premium = ['megasena', 'quina', 'lotofacil']

    for premium in list_premium:
        system(f'python download.py {premium}')

        logger.debug_register(f'Successfully created {premium} file!')

        logger.debug_register(
            f'Reading lake/{premium}/{now}/tratado.csv file...'
        )
        csv = read_csv(f'lake/{premium}/{now}/tratado.csv')

        data = csv.to_dict('records')
        # TODO: Fix data storage in Mongodb - (Delay)
        count = 0
        for row in data:
            db.insert(premium, row)
            count += 1
        logger.debug_register(
            f'Stored {premium} in the MongoDB! - {count} registers'
        )

    return render_template(
        'lotteries_caixa/index.html',
        message='Dados atualizados com sucesso',
        color='success',
    )
