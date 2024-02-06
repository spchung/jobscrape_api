from flask import request
from flask_restx import Resource, Namespace, fields
from .controller import *

api = Namespace('Jobs', description='CRUD Jobs')

QueryJobsModel = api.model('QueryJobsModel', {
    'job_id': fields.String,
    'company_id': fields.String,
    'title': fields.String,
    'job_type': fields.String,
    'location': fields.String,
    'salary': fields.String,
    'experience': fields.String,
    'education_restriction': fields.String,
    'subject_restriction': fields.String,
    'work_skills': fields.String,
    'technical_skills': fields.String,
    'addition_requirements': fields.String,
    'description': fields.String,
    'last_updated': fields.String,
    'source': fields.String
})

@api.route('/<id>')
class GetJobById(Resource):
    def get(self, id):
        return get_job_by_id(id), 200

@api.route('/')
class QueryJobs(Resource):
    @api.expect(QueryJobsModel)
    def post(self):
        payload = request.json
        return query_jobs(**payload), 200
