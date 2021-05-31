import logging
from datetime import datetime
from flask import Flask, jsonify, request
from analyzer import algorithms
from analyzer import constants
from analyzer import analyzer_utils
from analyzer import gateway


def process_dna(json_payload):
    dna = json_payload["dna"]
    valid_process = True
    try:

        if not analyzer_utils.is_valid(dna):
            jsonify({"Request error": constants.UNPROCESSABLE_ENTITY}), 422
        is_mutant = algorithms.is_mutant(dna)

    except Exception as error_instance:
        valid_process = False
        analyzer_utils.log_error(error_instance, constants.UNPROCESSABLE_ENTITY)

    if not valid_process:
        analyzer_utils.log_error(error_instance, constants.UNSUPPORTED_DATA_TYPE)
        return jsonify({"Unsuported data type error": constants.UNSUPPORTED_DATA_TYPE}), 415

    try:
        gateway.save_detection(dna, is_mutant)
    except Exception as error_instance:
        analyzer_utils.log_error(error_instance, constants.DATABASE_LAYER_ERROR)
        return (
            jsonify({f"is_mutant: {is_mutant}": constants.DATABASE_LAYER_ERROR}),
            502,
        )

    return jsonify({"is_mutant": is_mutant}), 200 if is_mutant else 403


def get_stats():
    mutants = gateway.get_mutant_count()
    humans = gateway.get_human_count()
    the_ratio = "undefined" if humans == 0 else mutants / float(humans)
    return jsonify({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": the_ratio})
