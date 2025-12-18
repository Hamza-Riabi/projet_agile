from PanierAchat import PanierAchat
from Produit import Produit
from PaiementParCompte import PaiementParCompte
from compte.compte_bancaire import CompteBancaire

def test_payer_panier_debite_compte():
    compte = CompteBancaire("Ali", 100)
    panier = PanierAchat()

    produit = Produit("Livre", 30, 10, True)
    panier.ajouter_produit(produit, 2)

    paiement = PaiementParCompte(compte)
    panier.payer(paiement)

    assert compte.solde == 40