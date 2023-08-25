from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def post(self):
        # Получение данных из запроса
        data = request.get_json()
        code_input = data.get("code", "")

        # Здесь будет логика вызова модели CodeLlama
        # Например:
        # output = model.predict(code_input)
        output = "Здесь будет вывод вашей модели на основе входных данных"

        return jsonify({"prediction": output})

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

