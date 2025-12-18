import unittest

from PanierAchat import PanierAchat
from Produit import Produit


class TestUS14AssociationBidirectionnelle(unittest.TestCase):

    def test_produit_connait_son_panier(self):
        panier = PanierAchat()
        produit = Produit("Livre", 10, 5, True)

        panier.ajouter_produit(produit, 1)

        self.assertEqual(produit.get_panier(), panier)


if __name__ == "__main__":
    unittest.main()
