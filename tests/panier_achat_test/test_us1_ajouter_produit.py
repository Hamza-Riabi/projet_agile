import unittest

from PanierAchat import PanierAchat
from Produit import Produit


class TestUS1AjouterProduit(unittest.TestCase):

    def test_ajout_produit_valide(self):
        panier = PanierAchat()
        produit = Produit("Livre", 15, 5, True)

        panier.ajouter_produit(produit, 2)

        self.assertEqual(1, len(panier.get_lignes()))
        self.assertEqual(2, panier.get_lignes()["Livre"].get_quantite())
        self.assertEqual(30, panier.calculer_total())


if __name__ == "__main__":
    unittest.main()
