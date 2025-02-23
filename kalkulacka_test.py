from unittest import TestCase
from kalkulacka import Kalkulacka

class TestKalkulacka(TestCase):
    def test_secti(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(kalkulacka.secti(5, 3), 8)
        self.assertEqual(kalkulacka.secti(105, 30), 135)

    def test_odecti(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(kalkulacka.odecti(5, 3), 2)
        self.assertEqual(kalkulacka.odecti(5, -3), 8)

    def test_vynasob(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(kalkulacka.vynasob(5, 3), 15)
        self.assertEqual(kalkulacka.vynasob(5, 5), 25)

    def test_vydel(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(kalkulacka.vydel(5, 5), 1)
