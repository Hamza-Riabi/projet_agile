import unittest

from PanierAchat import PanierAchat


class TestUS4ConsulterPanier(unittest.TestCase):

    def test_panier_vide(self):
        panier = PanierAchat()

        self.assertEqual(0, len(panier.get_lignes()))
        self.assertEqual(0, panier.calculer_total())


if __name__ == "__main__":
    unittest.main()
