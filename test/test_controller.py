import unittest
from analyzer import controller
from analyzer import constants


class ControllerFileTest(unittest.TestCase):
    def test_get_stats(self):
        mutants, humans, the_ratio = controller.get_stats()
        self.assertTrue(mutants >= 0)
        self.assertTrue(humans >= 0)

        pass

    def test_process_dna(self):
        message_key, message, code = controller.process_dna({"dnax": ["A"]})
        self.assertTrue(message_key == "Request error")
        self.assertTrue(message == constants.UNPROCESSABLE_ENTITY)
        self.assertTrue(code == 422)

        message_key, message, code = controller.process_dna({"dna": ["A"], "dummyfield": 3})
        self.assertTrue(message_key == "Request error")
        self.assertTrue(message == constants.UNPROCESSABLE_ENTITY)
        self.assertTrue(code == 422)

        message_key, message, code = controller.process_dna({})
        self.assertTrue(message_key == "Request error")
        self.assertTrue(message == constants.UNPROCESSABLE_ENTITY)
        self.assertTrue(code == 422)

        message_key, message, code = controller.process_dna({"AA"})
        self.assertTrue(message_key == "Request error")
        self.assertTrue(message == constants.UNPROCESSABLE_ENTITY)
        self.assertTrue(code == 422)

        message_key, message, code = controller.process_dna({"AA", "AB"})
        self.assertTrue(message_key == "Request error")
        self.assertTrue(message == constants.UNPROCESSABLE_ENTITY)
        self.assertTrue(code == 422)

        message_key, message, code = controller.process_dna({"dna": ["A"]})
        self.assertTrue(message_key == "is_mutant")
        self.assertTrue(message == False)
        self.assertTrue(code == 403)

        message_key, message, code = controller.process_dna({"dna": ["AAAA", "AAAA", "AAAA", "AAAA"]})
        self.assertTrue(message_key == "is_mutant")
        self.assertTrue(message == True)
        self.assertTrue(code == 200)

        pass


if __name__ == "__main__":
    unittest.main()
