class Produit:

    # Constructeur
    def __init__(self, nom, prix, stock, actif):
        self.nom = nom
        self.prix = prix
        self.stock = stock
        self.actif = actif
        self.panier = None # pour bidirectionnel 

    def get_nom(self):
        return self.nom

    def get_prix(self):
        return self.prix

    def get_stock(self):
        return self.stock

    def est_actif(self):
        return self.actif

    def retirer_stock(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite

    # pour bidirectionnel 
    def get_panier(self):
        return self.panier

    def _set_panier(self, panier):
        self.panier = panier

