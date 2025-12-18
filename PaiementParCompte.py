from PaiementStrategy import PaiementStrategy

class PaiementParCompte(PaiementStrategy):

    def __init__(self, compte_bancaire):
        self.compte_bancaire = compte_bancaire

    def payer(self, montant):
        self.compte_bancaire.retirer(montant)
