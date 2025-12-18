Feature: Consulter un panier
  En tant que client
  Je veux consulter mon panier
  Afin de voir son contenu

  Scenario: Consulter un panier vide
    Given un panier vide
    When je consulte le panier
    Then le panier est vide
