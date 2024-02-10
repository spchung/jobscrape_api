import importlib, os
from flask import Flask, url_for
from flask_restx import Api
from flask_cors import CORS, cross_origin
from shared.connection import db
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/v1/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'

class MyApi(Api):
    @property
    def specs_url(self):
        # Monkey patch for HTTPS
        scheme = 'http' if ('8080' in self.base_url or '5000' in self.base_url) else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)

swaggerApi = MyApi(
    app,
    version='1.0',
    title='Job Scrapper API',
    description='Expose Job search'
)

module_mapper = {
    'example': 'example',
    'jobs': 'jobs',
    'search': 'search'
}

sorted_moduleMapper = {}
for k, v in sorted(module_mapper.items(), key=lambda x: x[0]):
    sorted_moduleMapper[k] = v

for mod in sorted_moduleMapper:
    tmp = importlib.import_module("api." + mod + '.endpoint')
    swaggerApi.add_namespace(tmp.api, path='/v1/'+module_mapper[mod])

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)