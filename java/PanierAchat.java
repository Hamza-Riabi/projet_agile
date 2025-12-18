import java.util.HashMap;

public class PanierAchat {

    // Attributs : état du panier
    private HashMap<String, LignePanier> lignes;

    // Constructeur
    public PanierAchat() {
        lignes = new HashMap<>();
    }

    // Ajout d'un produit
    public void ajouterProduit(Produit produit, int quantite) {
        if (!produit.estActif() || quantite < 1 || quantite > produit.getStock()) {
            System.out.println("Impossible d'ajouter le produit : " + produit.getNom());
            return;
        }

        if (lignes.containsKey(produit.getNom())) {
            LignePanier ligne = lignes.get(produit.getNom());
            int nouvelleQte = ligne.getQuantite() + quantite;
            if (nouvelleQte > produit.getStock()) {
                System.out.println("Stock insuffisant pour " + produit.getNom());
                return;
            }
            ligne.setQuantite(nouvelleQte);
        } else {
            lignes.put(produit.getNom(), new LignePanier(produit, quantite));
        }
        System.out.println(quantite + " " + produit.getNom() + " ajoutés au panier.");
    }

    // Suppression d'un produit
    public void supprimerProduit(String nomProduit) {
        if (lignes.containsKey(nomProduit)) {
            lignes.remove(nomProduit);
            System.out.println(nomProduit + " supprimé du panier.");
        } else {
            System.out.println("Produit absent du panier.");
        }
    }

    // Calcul du total
    public double calculerTotal() {
        double total = 0;
        for (LignePanier ligne : lignes.values()) {
            total += ligne.getSousTotal();
        }
        return total;
    }

    // Affichage du panier
    public void afficherPanier() {
        if (lignes.isEmpty()) {
            System.out.println("Panier vide.");
            return;
        }
        for (LignePanier ligne : lignes.values()) {
            System.out.println(ligne);
        }
        System.out.println("Total général : " + calculerTotal());
    }

    // Getter pour tests unitaires
    public HashMap<String, LignePanier> getLignes() {
        return lignes;
    }
}