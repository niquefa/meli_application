import unittest
from analyzer import data_generator


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator(self):
        N = 20
        random_dna = data_generator.get_random_dna(N)
        for row in random_dna:
            self.assertTrue(N == len(row))
            for letter in row:
                self.assertTrue(letter in data_generator.LETTERS)
        pass


if __name__ == "__main__":
    unittest.main()
