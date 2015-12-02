from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app.scraper import getdata

# pantaupasar.org/api


app = Flask(__name__)
api = Api(app)

data = getdata()


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class GetSome(Resource):
    def get(self):
        return data
# 0.0.0.0/v2
api.add_resource(GetSome, '/v2')


if __name__ == '__main__':
    app.run(debug=True)
