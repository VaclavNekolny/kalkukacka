from unittest import TestCase
from kalkulacka import Kalkulacka

class TestKalkulacka(TestCase):
    def test_secti(self):

        kalkulacka = Kalkulacka()

        self.assertEqual(kalkulacka.secti(5, 3), 8)
        self.assertEqual(kalkulacka.odecti(5, 3), 2)