from PanierAchat import PanierAchat
from Produit import Produit
from compte.compte_bancaire import CompteBancaire

def test_paiement_panier_debite_compte():
    compte = CompteBancaire("Ali", 100)
    panier = PanierAchat()

    p1 = Produit("Livre", 30,5,True)
    panier.ajouter_produit(p1, 2)  # total = 60

    panier.payer(compte)

    assert compte.solde == 40
