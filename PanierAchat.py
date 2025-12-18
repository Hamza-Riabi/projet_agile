from LignePanier import LignePanier


class PanierAchat:

    # Constructeur
    def __init__(self):
        # Attributs : état du panier

        # --- techniques de refactoring (Rename) ---
        # Renommage de l'attribut "lignes" -> "lignes_panier" pour clarifier son rôle
        self.lignes_panier = {}

    # --- techniques de refactoring (Extract Method) ---
    # Extraction de la validation de quantité dans une méthode dédiée
    def _quantite_valide(self, produit, quantite):
        return produit.est_actif() and quantite >= 1 and quantite <= produit.get_stock()

    # Ajout d'un produit
    def ajouter_produit(self, produit, quantite):
        # Vérification association bidirectionnelle
        if produit.get_panier() is not None and produit.get_panier() is not self:
            print("Produit déjà associé à un autre panier")
            return

        # --- techniques de refactoring (Extract Method) ---
        # Remplace une condition complexe par un appel de méthode lisible
        if not self._quantite_valide(produit, quantite):
            print("Impossible d'ajouter le produit :", produit.get_nom())
            return

        nom_produit = produit.get_nom()

        if nom_produit in self.lignes_panier:
            ligne = self.lignes_panier[nom_produit]
            nouvelle_qte = ligne.get_quantite() + quantite
            if nouvelle_qte > produit.get_stock():
                print("Stock insuffisant pour", nom_produit)
                return
            ligne.set_quantite(nouvelle_qte)
        else:
            self.lignes_panier[nom_produit] = LignePanier(produit, quantite)

        produit._set_panier(self)   # bidirectionnel

        print(quantite, nom_produit, "ajoutés au panier.")

    # Suppression d'un produit
    # Modification pour bidirectionnel
    def supprimer_produit(self, nom_produit):
        if nom_produit in self.lignes_panier:
            ligne = self.lignes_panier[nom_produit]
            produit = ligne.produit
            produit._set_panier(None)
            del self.lignes_panier[nom_produit]
            print(nom_produit, "supprimé du panier.")
        else:
            print("Produit absent du panier.")

    # Calcul du total
    def calculer_total(self):
        total = 0.0
        for ligne in self.lignes_panier.values():
            total += ligne.get_sous_total()
        return total

    # Affichage du panier
    def afficher_panier(self):
        if not self.lignes_panier:
            print("Panier vide.")
            return

        for ligne in self.lignes_panier.values():
            print(ligne)

        print("Total général :", self.calculer_total())

    # Getter pour tests unitaires
    def get_lignes(self):
        return self.lignes_panier
