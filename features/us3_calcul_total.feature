Feature: Calculer le total du panier
  En tant que client
  Je veux connaître le total de mon panier
  Afin de vérifier le montant de ma commande

  Scenario Outline: Calculer le total avec plusieurs produits
    Given un panier contenant le produit "Livre" avec une quantité de 2
    Given un produit "<nom>" actif avec un prix de <prix> et un stock de <stock>
    When j'ajoute <quantite> exemplaires du produit "<nom>" au panier
    Then le total du panier est <total>

    Examples:
      | nom   | prix | stock | quantite | total |
      | Stylo | 5    | 10    | 1        | 35    |
      | Stylo | 5    | 10    | 2        | 40    |
