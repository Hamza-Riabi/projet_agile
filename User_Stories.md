
## **User Stories**

Les User Stories ci-dessous décrivent les besoins fonctionnels du système de panier d’achat.


### **US1 — Ajouter un produit au panier**

**En tant que** client
**Je veux** ajouter un produit actif au panier en précisant une quantité
**Afin de** préparer ma commande avec des produits disponibles.

**Critères d’acceptation :**

* Un produit ne peut être ajouté que s’il est **actif**.
* La quantité ajoutée doit être **supérieure ou égale à 1**.
* La quantité ajoutée ne peut pas dépasser le **stock disponible**.
* Si le produit est déjà présent dans le panier, la quantité est **incrémentée**.
* Une seule ligne de panier existe par produit.
* En cas de quantité invalide ou de stock insuffisant, l’ajout est refusé et le panier reste inchangé.

---

### **US2 — Supprimer un produit du panier**

**En tant que** client
**Je veux** supprimer un produit de mon panier
**Afin de** corriger mon choix avant la validation.

**Critères d’acceptation :**

* Si le produit est présent dans le panier, la ligne correspondante est supprimée.
* Si le produit est absent du panier, aucune modification n’est effectuée.
* Après suppression, le panier peut devenir vide.

---

### **US3 — Calculer le total du panier**

**En tant que** client
**Je veux** connaître le montant total de mon panier
**Afin de** évaluer le coût global de ma commande.

**Critères d’acceptation :**

* Le total du panier correspond à la somme des sous-totaux de chaque ligne.
* Le sous-total d’une ligne est égal à `prix unitaire × quantité`.
* Si le panier est vide, le total retourné est égal à `0`.
* Le total est recalculé à chaque modification du panier.

---

### **US4 — Consulter le contenu du panier**

**En tant que** client
**Je veux** consulter le contenu détaillé de mon panier
**Afin de** vérifier les produits et les montants avant validation.

**Critères d’acceptation :**

* Si le panier est vide, un message indiquant “Panier vide” est affiché.
* Chaque ligne de panier affiche : le nom du produit, le prix unitaire, la quantité et le sous-total.
* Le total général du panier est affiché à la fin de la consultation.

---

## US5 — Consulter le panier (détail des lignes)

**En tant que** client
**Je veux** consulter le contenu détaillé du panier
**Afin de** vérifier les produits et montants.

**Critères d’acceptation**

* Chaque ligne affiche : nom, prix unitaire, quantité, sous-total.
* Le total général est visible.
* Panier vide → message “Panier vide”.

---

## US6 — Valider la commande (hors paiement)

**En tant que** client
**Je veux** valider mon panier
**Afin de** transformer mon panier en commande.

**Critères d’acceptation**

* Un panier vide ne peut pas être validé.
* Avant validation : vérification globale (produits actifs, stocks suffisants, cohérence).
* Si validation réussie : une commande est créée/enregistrée, et le panier est verrouillé.
* Après verrouillage : aucune modification du panier n’est possible.

---

### **User Stories non implémentées à ce stade**

Les User Stories suivantes font partie du scénario global mais ne sont pas implémentées dans cette première itération :

* **Modification explicite de la quantité d’un produit**
* **Validation de la commande et verrouillage du panier**

Elles pourront être traitées lors d’itérations ultérieures.

