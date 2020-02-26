"""
high level support for doing this and that.
"""

from typing import Iterable
import logging
from flask import Flask, request, jsonify, make_response
from flask.logging import create_logger


APP = Flask(__name__)
LOG = create_logger(APP)
LOG.setLevel(logging.INFO)


@APP.route("/")
def home():
    """
    high level support for doing this and that.
    """
    html = f"<h3>Dummy Prediction</h3>"
    return html.format(format)


@APP.route("/predict", methods=["POST"])
def predict():
    """
    curl http://localhost:5000/score \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"X": [1, 2]}'
    """

    # Logging the input payload
    json_payload = request.json
    LOG.info("JSON payload: \n%s", json_payload)

    try:
        features = request.json["X"]
        prediction = model_predict(features)
        return make_response(jsonify({"json prediction content": prediction}))
    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')


def model_predict(my_list: Iterable[float]) -> Iterable[float]:
    """Dummy prediction function."""
    return my_list


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=80, debug=True)  # specify port=80
