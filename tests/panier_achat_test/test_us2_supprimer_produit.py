import unittest

from PanierAchat import PanierAchat
from Produit import Produit


class TestUS2SupprimerProduit(unittest.TestCase):

    def test_suppression_produit(self):
        panier = PanierAchat()
        produit = Produit("Livre", 15, 5, True)

        panier.ajouter_produit(produit, 2)
        panier.supprimer_produit("Livre")

        self.assertEqual(0, len(panier.get_lignes()))


if __name__ == "__main__":
    unittest.main()
