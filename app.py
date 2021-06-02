import os
import logging
import time
from datetime import datetime
from flask import Flask, jsonify, request
from analyzer import config
from analyzer import algorithms
from analyzer import controller

app = Flask(__name__)


@app.route("/health")
def health_check():
    return jsonify({"status": "the analyzer is healthy, nice problem! :)"})


@app.route("/mutant", methods=["POST"])
def mutant():
    message_key, message, code = controller.process_dna(request.get_json())
    return jsonify({message_key: message}), code


@app.route("/stats")
def stats():
    mutants, humans, the_ratio = controller.get_stats()
    return jsonify({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": the_ratio})


if __name__ == "__main__":

    if "ENVIRONMENT" in os.environ.keys() and os.environ["ENVIRONMENT"] == "TEST":
        logging.basicConfig(level=logging.INFO)
        app.run(host="127.0.0.1", port=3000)
    else:
        print(f"ANALIZER RUNNING logging level = logging.DEBUG")
        logging.basicConfig(level=logging.INFO)
        app.run(host="0.0.0.0", port=80)
