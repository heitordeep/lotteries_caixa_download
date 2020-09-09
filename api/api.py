from datetime import datetime as dt

from flask import Blueprint, jsonify, request

from db.connection import Database
from flask_restplus import Api, Resource

api_caixa = Blueprint('api', __name__)

rest_api = Api(
    api_caixa,
    version='1.0',
    title='Lotteries Caixa API',
    description='Handle list of awards',
    doc='/api/',
)

now = dt.now().strftime('%Y-%m-%d')
api = rest_api.namespace('api', description='GET method only')
db = Database()


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
            page = int(request.args.get('page', 1))

            limit = 150
            skip = limit * page

            # Search documents by collection.
            documents = db.find_content(premium, limit=limit, skip=skip)

            return jsonify(page=page, documents=documents)
        rest_api.abort(404, f"{premium} doesn't exist")

    @rest_api.response(403, 'Method Forbidden')
    def post(self, premium):
        rest_api.abort(403)

    @rest_api.response(403, 'Method Forbidden')
    def patch(self, premium):
        rest_api.abort(403)

    @rest_api.response(403, 'Method Forbidden')
    def put(self, premium):
        rest_api.abort(403)
