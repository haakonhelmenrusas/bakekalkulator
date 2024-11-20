import unittest
from bakekalkulator import Bakekalkulator

class TestBakekalkulator(unittest.TestCase):

    def setUp(self):
        self.porsjonerInn = 4
        self.ingredienser = [100, 200, 300]
        self.onsketAntallPorsjoner = 8
        self.bakekalkulator = Bakekalkulator(self.porsjonerInn, self.ingredienser, self.onsketAntallPorsjoner)

    def test_omdanningsfaktor(self):
        self.assertEqual(self.bakekalkulator.omdanningsfaktor(), 2.0)

    def test_nyListe(self):
        expected_list = [200, 400, 600]
        self.assertEqual(self.bakekalkulator.nyListe(), expected_list)

if __name__ == '__main__':
    unittest.main()
