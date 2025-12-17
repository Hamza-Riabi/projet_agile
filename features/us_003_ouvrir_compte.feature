Feature: US_003 Ouvrir un compte bancaire

En tant que Client
Je veux ouvrir un compte bancaire
Afin de commencer à gérer mon argent


Scenario Outline: ouverture de compte
  Given un client nommé <nom>
  When il ouvre un compte avec un solde initial de <solde_initial>
  Then un compte bancaire est créé
  And le solde du compte est égal à <solde_initial>

Examples:
  | nom   | solde_initial |
  | Sara  | 200           |
  | Ali   | 0             |