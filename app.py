from flask import Flask, request, jsonify, send_from_directory
import pickle

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
standard_scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")


@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    cgpa = float(data["cgpa"])
    iq = float(data["iq"])

    # Scale the input
    input_data = standard_scaler.transform([[cgpa, iq]])

    # Predict
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Placed"
    else:
        result = "Not Placed"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)