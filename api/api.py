from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    """
    Resource to handle predictions.
    """
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('code', type=str, required=True,
                               help='No code data provided', location='josn')

    
    def post(self):
        """
        Accepts JSON input with a 'code' key, and returns a prediction.
        """
        
        # Parse and validate incoming data
        try:
            args = self.reqparse.parse_args()
            code_input = args['code']

            # This simulates using a model to make predictions on the code_input
            # Ideally, you'd call your model here.
            output = f"Done: {code_input}. Here's your data."

            return jsonify({"prediction": output}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
