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
    return jsonify({"status": "the analyzer is healthy :)"})


@app.route("/mutant", methods=["POST"])
def mutant():
    message_key, message, code = controller.process_dna(request.get_json())
    return jsonify({message_key: message}), code


@app.route("/stats")
def stats():
    mutants, humans, the_ratio = controller.get_stats()
    return jsonify({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": the_ratio})


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    if "ENVIRONMENT" in os.environ.keys() and os.environ["ENVIRONMENT"] == "TEST":        
        logging.info("Running ENVIRONMENT TEST, HOST 127.0.0.1, and port 3000")
        app.run(host="127.0.0.1", port=3000)
    else:
        logging.info("Runing at host 0.0.0.0, and port 80")    
        app.run(host="0.0.0.0", port=80)
