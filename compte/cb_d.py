from compte.compte_bancaire import CompteBancaire


class CB_D(CompteBancaire):

    def retirer(self, montant: float) -> None:
        if self.titulaire is None:
            raise ValueError("aucun titulaire associé au compte")

        if montant <= 0:
            raise ValueError("montant invalide")

        if montant > self.solde:
            raise ValueError("solde insuffisant")

        super().retirer(montant)
