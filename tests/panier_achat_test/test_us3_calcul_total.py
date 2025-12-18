import unittest

from PanierAchat import PanierAchat
from Produit import Produit


class TestUS3CalculTotal(unittest.TestCase):

    def test_calcul_total_panier(self):
        panier = PanierAchat()

        livre = Produit("Livre", 15, 5, True)
        stylo = Produit("Stylo", 5, 10, True)

        panier.ajouter_produit(livre, 2)
        panier.ajouter_produit(stylo, 1)

        self.assertEqual(35, panier.calculer_total())


if __name__ == "__main__":
    unittest.main()
