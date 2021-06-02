import logging
from datetime import datetime
from flask import jsonify
from analyzer import algorithms
from analyzer import constants
from analyzer import analyzer_utils
from analyzer import gateway


def process_dna(json_payload):
    if "dna" not in json_payload or len(json_payload) != 1:
        return "Request error", constants.UNPROCESSABLE_ENTITY, 422

    dna = json_payload["dna"]

    if not analyzer_utils.is_valid(dna):
        return "Request error", constants.UNPROCESSABLE_ENTITY, 422

    try:
        is_mutant = algorithms.is_mutant(dna)
    except Exception as error_instance:
        analyzer_utils.log_error(error_instance, constants.ALGORITHM_LAYER_ERROR)
        return "Error", constants.ALGORITHM_LAYER_ERROR, 502

    try:
        gateway.save_detection(dna, is_mutant)
    except Exception as error_instance:
        analyzer_utils.log_error(error_instance, constants.DATABASE_LAYER_ERROR)
        return f"is_mutant: {is_mutant}", constants.DATABASE_LAYER_ERROR, 502

    return "is_mutant", is_mutant, 200 if is_mutant else 403


def get_stats():
    mutants = gateway.get_mutant_count()
    humans = gateway.get_human_count()
    the_ratio = "undefined" if humans == 0 else mutants / float(humans)
    return mutants, humans, the_ratio
