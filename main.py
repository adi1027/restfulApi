from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data":"helloworld"}
    def post(self):
        return {"data":"posted"}

api.add_resource(HelloWorld,"/helloworld")

if __name__=="__main__":
    app.run(debug=True)
