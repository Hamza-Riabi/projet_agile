public class LignePanier {

    private Produit produit;
    private int quantite;

    public LignePanier(Produit produit, int quantite) {
        this.produit = produit;
        this.quantite = quantite;
    }

    public int getQuantite() {
        return quantite;
    }

    public void setQuantite(int quantite) {
        this.quantite = quantite;
    }

    public double getSousTotal() {
        return produit.getPrix() * quantite;
    }

    @Override
    public String toString() {
        return produit.getNom() + " | Prix: " + produit.getPrix() + " | Qté: " + quantite + " | Sous-total: " + getSousTotal();
    }
}