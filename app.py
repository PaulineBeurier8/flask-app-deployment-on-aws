from flask import Flask, request, jsonify, make_response
from flask.logging import create_logger
import logging

from typing import Iterable

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = f"<h3>Dummy Prediction</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """
    curl http://localhost:5000/score \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"X": [1, 2]}'
    """

    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")

    try:
        features = request.json["X"]
        prediction = model_predict(features)
        return make_response(jsonify({"json prediction content": prediction}))
    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')


def model_predict(x: Iterable[float]) -> Iterable[float]:
    """Dummy prediction function."""
    return x


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)  # specify port=80
