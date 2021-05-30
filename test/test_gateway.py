import unittest
from analyzer import gateway
from analyzer import algorithms
from analyzer import data_generator


class GatewayTest(unittest.TestCase):
    def test_gateway_naive_tests(self):
        result = gateway.get_human_count()
        self.assertTrue(int(result) >= 0)
        result = gateway.get_mutant_count()
        self.assertTrue(int(result) >= 0)
        pass

    def test_gateway_upsert_dna(self):
        random_dna = data_generator.get_random_dna(20)
        self.assertTrue(len(random_dna) >= 0)

        is_mutant = algorithms.is_mutant(random_dna)

        old_count = gateway.get_processed_dna_count()

        gateway.save_detection(random_dna, is_mutant)

        total_dna = gateway.get_processed_dna_count()

        self.assertTrue(total_dna > old_count)
        pass


if __name__ == "__main__":
    unittest.main()
