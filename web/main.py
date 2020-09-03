from datetime import datetime as dt
from os import path

from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_parameter
from pandas import read_csv

from app.generate_csv import GeneratorCsv
from app.lotteries_download import CaixaLotteriesDownload

app = Blueprint(
    'web', __name__, url_prefix='/web/', template_folder='templates'
)

premium_allowed = ['megasena', 'lotofacil', 'quina']
now = dt.now().strftime('%Y-%m-%d')


@app.route('/')
def index():
    return render_template('lotteries_caixa/index.html')


@app.route('/result/<premium>/')
def view(premium):

    if premium in premium_allowed and path.exists(
        f'lake/{premium}/{now}/tratado.csv'
    ):

        PAGE_SIZE = 250
        csv = read_csv(f'lake/{premium}/{now}/tratado.csv')

        csv.sort_values(by=['Concurso'], inplace=True, ascending=False)

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


@app.route('/update/')
def update_csv():

    list_premium = ['megase', 'quina', 'lotfac']
    name = 'quina'

    for name_file in list_premium:
        url = f'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_{name_file}.zip'

        if name_file == 'megase':
            name = 'megasena'
        elif name_file == 'lotfac':
            name = 'lotofacil'

        get_file = CaixaLotteriesDownload(source_file=name, url=url)
        get_file.verification_http()
        create_csv = GeneratorCsv()
        create_csv.convert_to_csv(name, f'd_{name_file}')
        create_csv.sanitize_csv(name)
    return render_template(
        'lotteries_caixa/index.html',
        message='Dados atualizados com sucesso',
        color='success',
    )
