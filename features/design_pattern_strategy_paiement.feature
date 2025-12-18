Feature: US_020 Payer un panier

  En tant que Client
  Je veux payer mon panier
  Afin que le montant total soit débité de mon compte bancaire

  Scenario: Paiement d’un panier avecc solde suffisant
    Given un compte bancaire avec un solde initial de 100
    And un panier contenant un produit de prix 30 et quantité 2
    When le client paie le panier
    Then le solde du compte devient 40