from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app.scraper import getdata

# pantaupasar.org/api


app = Flask(__name__)
api = Api(app)

data = getdata()

class GetSome(Resource):
    def get(self):
        return data
        
# 0.0.0.0/v2
api.add_resource(GetSome, '/v2')


if __name__ == '__main__':
    app.run(debug=True)
