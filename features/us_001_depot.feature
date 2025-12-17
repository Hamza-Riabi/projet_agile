Feature: US_001 dépôt

En tant que Client
Je veux déposer et retirer de l’argent sur mon compte bancaire
Afin de gérer mon solde en toute sécurité


Scenario Outline: dépôt valide
  Given un compte bancaire avec un solde initial de <solde_initial>
  When l’utilisateur dépose <montant>
  Then le solde devient <solde_final>

Examples:
  | solde_initial | montant | solde_final |
  | 100           | 50      | 150         |
  | 0             | 20      | 20          |


Scenario Outline: refus de dépôt invalide
  Given un compte bancaire avec un solde initial de <solde_initial>
  When l’utilisateur dépose <montant>
  Then le système refuse avec le message <messageErreur>

Examples:
  | solde_initial | montant | messageErreur |
  | 100           | 0       | montant invalide |
  | 100           | -10     | montant invalide |
