from Produit import Produit

class LignePanier:

    # Constructeur
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def get_quantite(self):
        return self.quantite

    def set_quantite(self, quantite):
        self.quantite = quantite

    def get_sous_total(self):
        return self.produit.get_prix() * self.quantite

    def __str__(self):
        return (
            self.produit.get_nom()
            + " | Prix: "
            + str(self.produit.get_prix())
            + " | Qté: "
            + str(self.quantite)
            + " | Sous-total: "
            + str(self.get_sous_total())
        )
