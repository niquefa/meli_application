import logging
from datetime import datetime
from analyzer import constants


def is_valid(dna_matrix):
    N = len(dna_matrix)
    if N > constants.MAX_N_ALLOWED or N == 0:
        return False
    for row in dna_matrix:
        if N != len(row):
            return False
        for letter in row:
            if letter not in ["A", "C", "G", "T"]:
                return False
    return True


def log_error(error_instance, message):
    logging.error(
        {
            "log_time": datetime.utcnow(),
            "error_instance_type": type(error_instance),
            "error_instance_args": error_instance.args,
            "error_instance": error_instance,
        }
    )


def log_warning(message):
    logging.warning(
        {
            "log_time": datetime.utcnow(),
            "warning_message": message,
        }
    )
