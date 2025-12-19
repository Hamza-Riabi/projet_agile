from LignePanier import LignePanier


class PanierAchat:

    # Constructeur
    def __init__(self):
        self.lignes_panier = {}

    # Extraction de la validation de quantité dans une méthode dédiée
    def _quantite_valide(self, produit, quantite):
        return produit.est_actif() and 1 <= quantite <= produit.get_stock()

    # Ajout d'un produit
    def ajouter_produit(self, produit, quantite):
        if produit.get_panier() is not None and produit.get_panier() is not self:
            raise ValueError("Produit déjà associé à un autre panier")

        if not self._quantite_valide(produit, quantite):
            raise ValueError(f"Impossible d'ajouter le produit : {produit.get_nom()}")

        nom_produit = produit.get_nom()

        if nom_produit in self.lignes_panier:
            ligne = self.lignes_panier[nom_produit]
            nouvelle_qte = ligne.get_quantite() + quantite
            if nouvelle_qte > produit.get_stock():
                raise ValueError(f"Stock insuffisant pour {nom_produit}")
            ligne.set_quantite(nouvelle_qte)
        else:
            self.lignes_panier[nom_produit] = LignePanier(produit, quantite)

        produit._set_panier(self)

    # Suppression d'un produit
    def supprimer_produit(self, nom_produit):
        if nom_produit not in self.lignes_panier:
            raise KeyError("Produit absent du panier")

        ligne = self.lignes_panier[nom_produit]
        produit = ligne.produit
        produit._set_panier(None)
        del self.lignes_panier[nom_produit]

    # Calcul du total
    def calculer_total(self):
        return sum(ligne.get_sous_total() for ligne in self.lignes_panier.values())
    
    # Affichage du panier
    def afficher_panier(self):
        if not self.lignes_panier:
            return "Panier vide."

        lignes_txt = [str(l) for l in self.lignes_panier.values()]
        lignes_txt.append(f"Total général : {self.calculer_total()}")
        return "\n".join(lignes_txt)


    # Getter pour tests unitaires
    def get_lignes(self):
        return self.lignes_panier


    #avant design pattern stratégie de paiement : seulement compte bancaire est pris en considération
    # def payer(self, compte_bancaire):
    #     montant = self.calculer_total()
    #     compte_bancaire.retirer(montant)

    #nouveau méthode avec design pattern stratégie de paiement :
   	# Paiement du panier (Strategy)
    # Paiement du panier (Strategy)
    # Paiement du panier (Strategy)
    def payer(self, paiement_strategy):
        montant = self.calculer_total()
        paiement_strategy.payer(montant)
