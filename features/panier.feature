Feature: Gestion du panier d'achat
  Le client peut gérer un panier d'achat en respectant les règles métier
  (stock, produit actif, calcul du total).

  Scenario: US1 - Ajouter un produit au panier
    Given un panier vide
    And un produit "Livre" actif avec un prix de 15 et un stock de 5
    When j'ajoute 2 exemplaires du produit "Livre" au panier
    Then le panier contient 1 ligne
    And la quantité du produit "Livre" est 2
    And le total du panier est 30

  Scenario: US2 - Supprimer un produit du panier
    Given un panier contenant le produit "Livre" avec une quantité de 2
    When je supprime le produit "Livre" du panier
    Then le panier est vide

  Scenario: US3 - Calculer le total du panier
    Given un panier contenant le produit "Livre" avec une quantité de 2
    And un produit "Stylo" actif avec un prix de 5 et un stock de 10
    When j'ajoute 1 exemplaire du produit "Stylo" au panier
    Then le total du panier est 35

  Scenario: US4 - Consulter un panier vide
    Given un panier vide
    When je consulte le panier
    Then le panier est vide
