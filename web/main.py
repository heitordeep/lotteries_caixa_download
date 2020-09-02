from datetime import datetime as dt
from glob import glob

from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_parameter
from pandas import read_csv

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

    if premium in premium_allowed:

        search = False
        q = request.args.get('q')
        PAGE_SIZE = 250

        if q:
            search = True

        csv = read_csv(f'lake/{premium}/{now}/tratado.csv')

        csv.sort_values(by=['Concurso'], inplace=True, ascending=False)

        page = request.args.get(get_page_parameter(), type=int, default=1)

        row_data = csv[
            (page - 1) * PAGE_SIZE : page * PAGE_SIZE
        ].values.tolist()

        pagination = Pagination(
            page=page,
            total=len(csv),
            search=search,
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
        'lotteries_caixa/index.html', error=f'Not Found element {premium}!'
    )
