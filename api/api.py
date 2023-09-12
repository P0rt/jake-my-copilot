from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def post(self):
        
        data = request.get_json(force=True)  
        code_input = data.get("code", "")

        # This for example CodeLlama
        # Example:
        # output = model.predict(code_input)
        output = f"Done: {code_input}. Here your data."

        return jsonify({"prediction": output})

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
