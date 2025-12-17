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
        context.client.ouvrir_compte(solde_initial)
    except Exception as e:
        context.exception = e


# -------- THEN --------

@then("un compte bancaire est créé")
def step_then_compte_cree(context):
    assert context.client.compte is not None


@then("le solde du compte est égal à {solde_initial:d}")
def step_then_solde_compte(context, solde_initial):
    assert context.client.compte.solde == solde_initial
    

