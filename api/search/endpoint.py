from flask import request
from flask_restx import Resource, Namespace, fields
from .controller import *

api = Namespace('Search', description='vector operations for job search')

QueryJobsDescModel = api.model('QueryJobsDescModel', {
    'search_term': fields.String
})

QueryJobstitleModel = api.model('QueryJobstitleModel', {
    'search_term': fields.String
})

ComboModel = api.model('ComboModel', {
    'title': fields.String,
    'description': fields.String
})

@api.route('/')
class QueryJobs(Resource):
    @api.expect(ComboModel)
    def post(self):
        payload = request.json
        if 'title' in payload and 'description' in payload:
            return search_title_and_description(payload['title'], payload['description']), 200
        return 'Invalid', 400
    
@api.route('/title')
class QueryJobstitle(Resource):
    def post(self):
        payload = request.json
        if 'search_term' in payload:
            return search_title(payload['search_term']), 200
        return 'Invalid', 400

@api.route('/description')
class QueryJobsDesc(Resource):
    @api.expect(QueryJobsDescModel)
    def post(self):
        payload = request.json
        if 'search_term' in payload:
            return search_description(payload['search_term']), 200
        return 'Invalid', 400

