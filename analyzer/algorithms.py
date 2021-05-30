import logging
from analyzer import analyzer_utils
from analyzer import constants

# In this mutant detection function, the two sequences to search could overlap in one or more position
def is_mutant(dna):
    if not analyzer_utils.is_valid(dna):
        log_dictionary = {"category": constants.INVALID_DNA_SAMPLE, "data": dna}
        analyzer_utils.log_warning(log_dictionary)
        raise Exception(f"{log_dictionary}")
        return False
    N = len(dna)
    if N < 4:
        return False
    detections = 0
    for i in range(N):
        for j in range(N):
            c = dna[i][j]
            if (
                j - 3 >= 0
                and i - 3 >= 0
                and c == dna[i - 1][j - 1]
                and c == dna[i - 2][j - 2]
                and c == dna[i - 3][j - 3]
            ):
                detections += 1
            if detections > 1:
                return True

            if j - 3 >= 0 and c == dna[i][j - 1] and c == dna[i][j - 2] and c == dna[i][j - 3]:
                detections += 1
            if detections > 1:
                return True

            if i - 3 >= 0 and c == dna[i - 1][j] and c == dna[i - 2][j] and c == dna[i - 3][j]:
                detections += 1
            if detections > 1:
                return True

    return False
