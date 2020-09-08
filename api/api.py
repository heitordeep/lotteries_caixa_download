import json
from datetime import datetime as dt
from os import path

from flask import Blueprint, jsonify
from flask_restplus import Api, Resource
from pandas import read_csv

api_caixa = Blueprint('api', __name__, url_prefix='/api')

rest_api = Api(
    api_caixa,
    version='1.0',
    title='Lotteries Caixa API',
    description='List of Caixa Economica Federal prizes',
)


now = dt.now().strftime('%Y-%m-%d')

api = rest_api.namespace('api', description='GET method only')


@api.route('/<premium>/')
@api.doc(
    params={
        'premium': 'Enter the names of the prizes: mega sena, lotofacil or quina'
    },
)
class LotteriesCaixaApi(Resource):
    def get(self, premium):

        premium_allowed = ['megasena', 'lotofacil', 'quina']

        if premium in premium_allowed:

            if path.exists(f'lake/{premium}/{now}/tratado.csv'):

                csv = read_csv(f'lake/{premium}/{now}/tratado.csv')
                csv.sort_values(by=['Concurso'], inplace=True, ascending=False)

                csv = csv[csv['Cidade'].notna()]
                csv = csv[csv['UF'].notna()]

                return jsonify(json.loads(csv.to_json(orient='records')))
            rest_api.abort(404, f'Not found data in the date: {now}')
        rest_api.abort(404, f"{premium} doesn't exist")

    @rest_api.response(403, 'Not Authorized')
    def post(self, premium):
        rest_api.abort(403)

    @rest_api.response(403, 'Not Authorized')
    def patch(self, premium):
        rest_api.abort(403)

    @rest_api.response(403, 'Not Authorized')
    def put(self, premium):
        rest_api.abort(403)
