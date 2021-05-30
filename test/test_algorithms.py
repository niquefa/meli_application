import unittest
from analyzer import algorithms


class AlgorithmsTest(unittest.TestCase):
    def test_algorithms_naive_cases(self):
        self.assertFalse(algorithms.is_mutant(["ATG", "CAG", "TTA"]))
        self.assertFalse(algorithms.is_mutant(["CA", "TA"]))
        self.assertFalse(algorithms.is_mutant(["C"]))
        self.assertFalse(algorithms.is_mutant([]))
        pass

    def test_algorithms_problem_description_samples(self):
        human_dna = ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
        self.assertFalse(algorithms.is_mutant(human_dna))

        mutant_dna = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG",
        ]
        self.assertTrue(algorithms.is_mutant(mutant_dna))
        pass

    def test_algorithms_small_cases(self):
        human_dna = ["AGTC", "GTAC", "TTGA", "AGTC"]
        self.assertFalse(algorithms.is_mutant(human_dna))

        mutant_dna = ["AAAA", "CCCC", "TTTT", "GGGG"]
        self.assertTrue(algorithms.is_mutant(mutant_dna))

        mutant_dna = ["TATA", "TCCA", "TGAA", "TGGA"]
        self.assertTrue(algorithms.is_mutant(mutant_dna))

        pass


if __name__ == "__main__":
    unittest.main()
