# Storytelling unifié – Du panier à la trésorerie

## Une histoire commune (le fil rouge)

Notre projet raconte l’histoire d’un client sur une plateforme e-commerce, depuis l’intention d’achat jusqu’à la maîtrise de son budget.

Tout commence côté boutique : le client parcourt un catalogue et construit son **panier d’achat**. Il ajoute des produits, en supprime, consulte le contenu et vérifie le **montant total**. Le panier joue le rôle de “mémoire” des choix effectués avant toute décision finale.

Mais une question revient systématiquement au moment de finaliser l’achat : **ai-je les moyens ?**  
C’est là que le second univers entre en scène : le **CompteBancaire**. Il représente la capacité du client à financer ses achats. Il permet de déposer, retirer, contrôler des règles simples (montant valide, solde suffisant) et sécurise l’idée qu’un achat n’est possible que si la trésorerie suit.

Notre fusion consiste donc à relier deux réalités complémentaires :
- le **panier** répond à : *“Qu’est-ce que je veux acheter ? Combien ça coûte ?”*
- le **compte bancaire** répond à : *“Puis-je me le permettre ? Quelles règles protègent les opérations ?”*

L’objectif n’est pas de construire un site e-commerce complet, mais un **mini-univers pédagogique** : des objets simples, des règles explicites, des tests qui garantissent que l’histoire reste cohérente.

---

## Description du projet (vision vulgarisée)

Le projet est composé de deux modules qui se complètent.

### Module A – Panier d’achat

Le panier permet au client de :
- ajouter un produit actif (avec stock suffisant),
- supprimer un produit,
- consulter le contenu,
- calculer le total (somme des sous-totaux).

Règles clés :
- un produit doit être **actif** pour être ajouté,
- la quantité ajoutée doit être comprise entre **1** et le **stock disponible**,
- une seule **ligne de panier** existe par produit,
- le total du panier est recalculé après chaque action,
- un panier peut être vide.

### Module B – Compte bancaire

Le compte bancaire permet au client de :
- déposer une somme,
- retirer une somme,
- empêcher les opérations incohérentes (montant invalide, solde insuffisant).

Règles clés :
- montant strictement positif,
- retrait impossible si le solde n’est pas suffisant.

---

## Comment les deux se rencontrent (la collaboration)

La fusion donne un scénario “réaliste” et simple :

1. Le client construit un panier (monde e-commerce).
2. Il consulte le total (toujours e-commerce).
3. Il compare ce total à son solde (monde bancaire).
4. Option pédagogique : une action “collaborative” peut être simulée, par exemple :
   - **pré-validation du budget** : “Le total du panier est-il finançable ?”
   - ou **tentative de débit** (si souhaité), sans implémenter tout le paiement.

Cette collaboration est idéale pour le TP, car elle illustre clairement :
- deux objets différents,
- une interaction entre eux,
- des tests qui protègent le comportement global.

