---

## **🎯 Intitulé**

Gestion du panier d’achat

---

## **👤 Rôle**

*En tant que* client d’une plateforme e-commerce,
*Je veux* pouvoir gérer un panier d’achat (ajout, suppression, consultation),
*Afin de* connaître à tout moment le contenu et le montant total de mes achats.

---

## **🧩 Contexte métier**

Le panier d’achat permet de regrouper les produits sélectionnés par un utilisateur avant une éventuelle commande.
Il constitue une étape essentielle entre la consultation du catalogue et la validation finale.

---

## **📌 Périmètre fonctionnel**

Fonctionnalités couvertes dans ce projet :

* ajout de produits au panier
* suppression de produits
* calcul du total du panier
* consultation du panier

Fonctionnalités hors périmètre :

* modification avancée des quantités
* validation de la commande
* paiement, livraison et facturation

---

## **⚙️ Règles métier**

* un produit doit être actif pour être ajouté au panier
* la quantité ajoutée doit être comprise entre 1 et le stock disponible
* une seule ligne de panier existe par produit
* le total du panier est recalculé après chaque action
* un panier peut être vide

---

## **🧪 Scénarios & critères d’acceptation**

### **Scénario 1 – Ajouter un produit au panier (US1)**

*Étant donné* un panier vide
*Et* un produit actif disponible en stock
*Quand* l’utilisateur ajoute le produit au panier
*Alors* :

* le produit est ajouté au panier
* une ligne de panier est créée
* le total du panier est mis à jour

---

### **Scénario 2 – Supprimer un produit du panier (US2)**

*Étant donné* un panier contenant un produit
*Quand* l’utilisateur supprime ce produit
*Alors* :

* la ligne de panier est supprimée
* le panier est mis à jour
* le panier peut devenir vide

---

### **Scénario 3 – Calculer le total du panier (US3)**

*Étant donné* un panier contenant plusieurs produits
*Quand* l’utilisateur consulte le total
*Alors* :

* le montant total correspond à la somme des sous-totaux des produits

---

### **Scénario 4 – Consulter un panier (US4)**

*Étant donné* un panier existant
*Quand* l’utilisateur consulte son panier
*Alors* :

* le contenu du panier est affiché
* le total général est visible
  *Et si le panier est vide* :
* un message indiquant que le panier est vide est affiché

---

## **🧪 Stratégie de tests**

### **Tests unitaires**

* ajout d’un produit
* suppression d’un produit
* calcul du total
* état d’un panier vide

### **Tests fonctionnels (BDD)**

* validation des scénarios US1 à US4 à partir de fichiers `.feature`
* vérification du comportement global du panier

---

