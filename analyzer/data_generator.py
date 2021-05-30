import random

LETTERS = ["A", "C", "G", "T"]


def get_random_dna(size):
    dna = []
    for i in range(size):
        row = ""
        for j in range(size):
            row += LETTERS[random.randint(0, len(LETTERS) - 1)]
        dna.append(row)
    return dna
