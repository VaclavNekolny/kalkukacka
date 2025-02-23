from unittest import TestCase
from hesla import Validator

class TestValidatoru(TestCase):
    def test_validni_heslo(self):
        validator = Validator()
        self.assertTrue(validator.validuj_heslo("ahoj1"), True)

    def test_kratke_heslo(self):
        validator = Validator()
        self.assertTrue(validator.validuj_heslo("ah1"), True)

    def test_heslo_bez_cislice(self):
        validator = Validator()
        self.assertTrue(validator.validuj_heslo("ahojhfg"), True)

    def test_prazdne_heslo(self):
        validator = Validator()
        self.assertTrue(validator.validuj_heslo(""), True)

if __name__ == '__main__':unittest.main()