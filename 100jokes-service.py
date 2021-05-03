from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/jokes', methods=['GET'])
class JokesTop100(Resource):
    def get(self):
        jokes = {}
        number = 1

@api.route('/health', methods=['GET'])
class CheckHealth(Resource):
    def get(self):
        return 'healthy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')
