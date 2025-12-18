Feature: Ajouter un produit au panier
  En tant que client
  Je veux ajouter un produit à mon panier
  Afin de constituer une commande

  Scenario Outline: Ajouter un produit actif avec stock suffisant
    Given un panier vide
    Given un produit "<nom>" actif avec un prix de <prix> et un stock de <stock>
    When j'ajoute <quantite> exemplaires du produit "<nom>" au panier
    Then le panier contient 1 ligne
    Then la quantité du produit "<nom>" est <quantite>
    Then le total du panier est <total>

    Examples:
      | nom   | prix | stock | quantite | total |
      | Livre | 15   | 5     | 2        | 30    |
      | Stylo | 5    | 10    | 3        | 15    |
