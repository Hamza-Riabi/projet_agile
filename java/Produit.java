public class Produit {

    private String nom;
    private double prix;
    private int stock;
    private boolean actif;

    public Produit(String nom, double prix, int stock, boolean actif) {
        this.nom = nom;
        this.prix = prix;
        this.stock = stock;
        this.actif = actif;
    }

    public String getNom() {
        return nom;
    }

    public double getPrix() {
        return prix;
    }

    public int getStock() {
        return stock;
    }

    public boolean estActif() {
        return actif;
    }

    public void retirerStock(int quantite) {
        if (quantite <= stock) {
            stock -= quantite;
        }
    }
}