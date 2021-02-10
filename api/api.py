from flask import Blueprint, jsonify, request
from flask_restplus import Api, Resource

from db.connection import Database

api_caixa = Blueprint('api', __name__)

rest_api = Api(
    api_caixa,
    version='1.0',
    title='Lotteries Caixa API',
    description='Handle list of prizes',
    doc='/api/',
)

api = rest_api.namespace('api', description='GET method only')
db = Database()


@api.route('/<prize>')
@api.doc(
    params={
        'prize': 'Enter the names of the prizes: mega sena, lotofacil or quina. Return default: 300 element.'
    },
)
class HandleAllPrizes(Resource):
    def get(self, prize):

        prize_allowed = ['megasena', 'lotofacil', 'quina']
        limit_allowed = 300

        if prize in prize_allowed:
            limit = int(request.args.get('limit', limit_allowed))
            term = request.args.get('term', 'data_sorteio')
            search = request.args.get('search', {'$gt': '01/01/1900'})

            # Search documents by collection and term.
            query = {term: search}

            documents = db.find_content(query, prize, limit=limit)

            return jsonify(count_data=len(documents), documents=documents)
        rest_api.abort(404, f"{prize} doesn't exist!")

    @rest_api.response(403, 'Method Forbidden!')
    def post(self, prize):
        rest_api.abort(403)

    @rest_api.response(403, 'Method Forbidden!')
    def patch(self, prize):
        rest_api.abort(403)

    @rest_api.response(403, 'Method Forbidden!')
    def put(self, prize):
        rest_api.abort(403)
