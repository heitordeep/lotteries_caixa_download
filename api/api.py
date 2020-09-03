import json
from datetime import datetime as dt
from os import path

from flask import Blueprint, jsonify

from pandas import read_csv

api = Blueprint('api', __name__, url_prefix='/api/')

now = dt.now().strftime('%Y-%m-%d')


@api.route('/<premium>/')
def index(premium):

    if path.exists(f'lake/{premium}/{now}/tratado.csv'):

        csv = read_csv(f'lake/{premium}/{now}/tratado.csv')
        csv.sort_values(by=['Concurso'], inplace=True, ascending=False)

        csv = csv[csv['Cidade'].notna()]
        csv = csv[csv['UF'].notna()]

        return jsonify(json.loads(csv.to_json(orient='records')))
