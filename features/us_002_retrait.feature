Feature: US_002 Retirer de l’argent d’un compte bancaire

En tant que Client
Je veux retirer de l’argent de mon compte bancaire
Afin d’utiliser mon solde disponible


Scenario Outline: retrait valide
  Given un compte bancaire avec un solde initial de <solde_initial>
  When l’utilisateur retire <montant>
  Then le solde devient <solde_final>

Examples:
  | solde_initial | montant | solde_final |
  | 200           | 50      | 150         |
  | 100           | 100     | 0           |


Scenario Outline: refus de retrait invalide
  Given un compte bancaire avec un solde initial de <solde_initial>
  When l’utilisateur retire <montant>
  Then le système refuse avec le message <messageErreur>

Examples:
  | solde_initial | montant | messageErreur       |
  | 100           | -10     | montant invalide    |
  | 100           | 200     | solde insuffisant   |