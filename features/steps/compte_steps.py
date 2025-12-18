from behave import given, when, then
from compte.compte_bancaire import CompteBancaire
from PanierAchat import PanierAchat
from Produit import Produit
from PaiementParCompte import PaiementParCompte



# -------- GIVEN --------

@given("un compte bancaire avec un solde initial de {solde_initial:d}")
def step_given_compte(context, solde_initial):
    context.compte = CompteBancaire("Client", solde_initial)
    context.exception = None


# -------- WHEN --------

@when("l’utilisateur dépose {montant:d}")
def step_when_deposer(context, montant):
    try:
        context.compte.deposer(montant)
    except Exception as e:
        context.exception = e


@when("l’utilisateur retire {montant:d}")
def step_when_retirer(context, montant):
    try:
        context.compte.retirer(montant)
    except Exception as e:
        context.exception = e


# -------- THEN --------

@then("le solde devient {solde_final:d}")
def step_then_solde(context, solde_final):
    assert context.compte.solde == solde_final


@then("le système refuse avec le message {messageErreur}")
def step_then_refus(context, messageErreur):
    assert context.exception is not None
    assert messageErreur in str(context.exception)






#OUVRIR COMPTE 
from compte.client import Client

# -------- GIVEN --------

@given("un client nommé {nom}")
def step_given_client(context, nom):
    context.client = Client(nom)
    context.exception = None


# -------- WHEN --------

@when("il ouvre un compte avec un solde initial de {solde_initial:d}")
def step_when_ouvrir_compte(context, solde_initial):
    try:
        context.compte = context.client.ouvrir_compte(solde_initial)
    except Exception as e:
        context.exception = e


# -------- THEN --------

@then("un compte bancaire est créé")
def step_then_compte_cree(context):
    assert len(context.client.comptes) == 1


@then("le solde du compte est égal à {solde_initial:d}")
def step_then_solde_compte(context, solde_initial):
    assert context.compte.solde == solde_initial
























from PanierAchat import PanierAchat
from Produit import Produit


# GIVEN


@given("un panier vide")
def step_panier_vide(context):
    context.panier = PanierAchat()
    context.produits = {}


@given('un produit "{nom}" actif avec un prix de {prix:d} et un stock de {stock:d}')
def step_creer_produit(context, nom, prix, stock):
    produit = Produit(nom, prix, stock, True)

    if not hasattr(context, "produits") or context.produits is None:
        context.produits = {}

    context.produits[nom] = produit


@given('un panier contenant le produit "{nom}" avec une quantité de {quantite:d}')
def step_panier_avec_produit(context, nom, quantite):
    context.panier = PanierAchat()
    context.produits = {}

    # Prix/stock par défaut pour ce Given (suffisant pour les scénarios)
    produit = Produit(nom, 15, 50, True)
    context.produits[nom] = produit

    context.panier.ajouter_produit(produit, quantite)

# WHEN


@when('j\'ajoute {quantite:d} exemplaires du produit "{nom}" au panier')
@when('j\'ajoute {quantite:d} exemplaire du produit "{nom}" au panier')
def step_ajouter_produit(context, quantite, nom):
    produit = context.produits[nom]
    context.panier.ajouter_produit(produit, quantite)


@when('je supprime le produit "{nom}" du panier')
def step_supprimer_produit(context, nom):
    context.panier.supprimer_produit(nom)


@when("je consulte le panier")
def step_consulter_panier(context):
    # On l'appelle, mais les asserts sont faits dans les Then
    context.panier.afficher_panier()

# THEN


@then("le panier contient {nb:d} ligne")
def step_verifier_nombre_lignes(context, nb):
    assert len(context.panier.get_lignes()) == nb


@then('la quantité du produit "{nom}" est {quantite:d}')
def step_verifier_quantite(context, nom, quantite):
    assert context.panier.get_lignes()[nom].get_quantite() == quantite


@then("le panier est vide")
def step_panier_est_vide(context):
    assert len(context.panier.get_lignes()) == 0


@then("le total du panier est {total:d}")
def step_verifier_total(context, total):
    assert context.panier.calculer_total() == total




#design pattern paiement test

@given("un compte bancaire avecc un solde initial de {solde:d}")
def step_compte(context, solde):
    context.compte = CompteBancaire("ClientTest", solde)


@given("un panier contenant un produit de prix {prix:d} et quantité {quantite:d}")
def step_panier(context, prix, quantite):
    context.panier = PanierAchat()
    produit = Produit("ProduitTest", prix, 10, True)
    context.panier.ajouter_produit(produit, quantite)


@when("le client paie le panier")
def step_payer_panier(context):
    paiement = PaiementParCompte(context.compte)
    context.panier.payer(paiement)


@then("le solde du compte devient {solde_final:d}")
def step_verifier_solde(context, solde_final):
    assert context.compte.solde == solde_final    
