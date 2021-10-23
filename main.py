from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"Message":"HelloWorld"}
    
    def post(self):
        return {'Message': "posted"}

api.add_resource(HelloWorld,"/")
if __name__ == "__main__":
    app.run(debug=True)