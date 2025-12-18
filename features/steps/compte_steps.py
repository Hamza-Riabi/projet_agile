from behave import given, when, then
from compte.compte_bancaire import CompteBancaire

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


@given("un panier vide")
def step_panier_vide(context):
    context.panier = PanierAchat()


@given('un produit "{nom}" actif avec un prix de {prix:d} et un stock de {stock:d}')
def step_creer_produit(context, nom, prix, stock):
    produit = Produit(nom, prix, stock, True)
    context.produits = getattr(context, "produits", {})
    context.produits[nom] = produit


@given('un panier contenant le produit "{nom}" avec une quantité de {quantite:d}')
def step_panier_avec_produit(context, nom, quantite):
    context.panier = PanierAchat()
    produit = Produit(nom, 15, 10, True)
    context.produits = {nom: produit}
    context.panier.ajouter_produit(produit, quantite)


@when('j\'ajoute {quantite:d} exemplaire du produit "{nom}" au panier')
@when('j\'ajoute {quantite:d} exemplaires du produit "{nom}" au panier')
def step_ajouter_produit(context, quantite, nom):
    produit = context.produits[nom]
    context.panier.ajouter_produit(produit, quantite)



@when('je supprime le produit "{nom}" du panier')
def step_supprimer_produit(context, nom):
    context.panier.supprimer_produit(nom)


@when("je consulte le panier")
def step_consulter_panier(context):
    context.panier.afficher_panier()


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

