Feature: US_020 Payer un panier

  En tant que Client
  Je veux payer mon panier
  Afin que le montant total soit débité de mon compte bancaire

  Scenario: Paiement d’un panier avecc solde suffisant
    Given un compte bancaire avec un solde initial de 100
    And un panier contenant un produit de prix 30 et quantité 2
    When le client paie le panier
    Then le solde du compte devient 40
    
  Scenario: Paiement refusé faute de solde suffisant
    Given un compte bancaire avec un solde initial de 20
    And un panier contenant un produit de prix 30 et quantité 1
    When le client tente de payer le panier
    Then le paiement est refusé
    And le solde du compte reste 20


      