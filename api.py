from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello, World!"

class Predict(Resource):
    def post(self):
        # Получение данных из запроса
        data = request.get_json(force=True)  # Добавим force=True, чтобы попытаться разобрать данные даже если нет заголовка Content-Type
        code_input = data.get("code", "")

        # Здесь будет логика вызова модели CodeLlama
        # Например:
        # output = model.predict(code_input)
        output = f"Принято: {code_input}. Здесь будет вывод вашей модели на основе входных данных."

        return jsonify({"prediction": output})

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
