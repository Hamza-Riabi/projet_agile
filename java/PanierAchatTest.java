import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PanierAchatTest {

    @Test
    public void testAjouterProduit() {
        PanierAchat panier = new PanierAchat();
        Produit livre = new Produit("Livre", 15.0, 5, true);
        panier.ajouterProduit(livre, 2);

        assertEquals(1, panier.getLignes().size());
        assertEquals(2, panier.getLignes().get("Livre").getQuantite());
        assertEquals(30.0, panier.calculerTotal());
    }

    @Test
    public void testSuppressionProduit() {
        PanierAchat panier = new PanierAchat();
        Produit livre = new Produit("Livre", 15.0, 5, true);
        panier.ajouterProduit(livre, 2);
        panier.supprimerProduit("Livre");

        assertEquals(0, panier.getLignes().size());
    }

    @Test
    public void testStockInsuffisant() {
        PanierAchat panier = new PanierAchat();
        Produit souris = new Produit("Souris", 50.0, 1, true);
        panier.ajouterProduit(souris, 2); // > stock
        assertEquals(0, panier.getLignes().size());
    }
}