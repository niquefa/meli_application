import unittest
from analyzer import analyzer_utils


class AnalyzerUtilsTest(unittest.TestCase):
    def test_analyzer_utils(self):
        valid_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        self.assertTrue(analyzer_utils.is_valid(valid_dna))
        invalid_dna = ["XTGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        self.assertFalse(analyzer_utils.is_valid(invalid_dna))
        invalid_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACT"]
        self.assertFalse(analyzer_utils.is_valid(invalid_dna))
        invalid_dna = ["aTGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTAa"]
        self.assertFalse(analyzer_utils.is_valid(invalid_dna))

        pass


if __name__ == "__main__":
    unittest.main()
