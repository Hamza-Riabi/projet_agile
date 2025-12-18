Feature: Supprimer un produit du panier
  En tant que client
  Je veux supprimer un produit de mon panier
  Afin de modifier ma commande

  Scenario: Supprimer un produit existant du panier
    Given un panier contenant le produit "Livre" avec une quantité de 2
    When je supprime le produit "Livre" du panier
    Then le panier est vide
