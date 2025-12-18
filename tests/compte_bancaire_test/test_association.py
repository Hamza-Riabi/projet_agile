from compte.client import Client
from compte.compte_bancaire import CompteBancaire

#Un client peut ouvrir plusieurs comptes
def test_client_peut_ouvrir_plusieurs_comptes():
    client = Client("Hamza")

    c1 = client.ouvrir_compte(100)
    c2 = client.ouvrir_compte(300)

    assert len(client.comptes) == 2
    assert c1 in client.comptes
    assert c2 in client.comptes

#Chaque compte a bien le bon titulaire
def test_compte_a_un_seul_titulaire():
    client = Client("Hamza")
    compte = client.ouvrir_compte(200)

    assert compte.titulaire == client

#Un compte ne peut pas exister sans client (robustesse 0..1)
def test_compte_peut_exister_sans_titulaire():
    compte = CompteBancaire()
    assert compte.titulaire is None

#Les soldes sont indépendants entre comptes    
def test_soldes_independants_entre_comptes():
    client = Client("Hamza")

    c1 = client.ouvrir_compte(100)
    c2 = client.ouvrir_compte(500)

    c1.deposer(50)

    assert c1.solde == 150
    assert c2.solde == 500

#Retrait sur un compte n’impacte pas les autres
def test_operations_sur_un_compte_n_affectent_pas_les_autres():
    client = Client("Hamza")

    c1 = client.ouvrir_compte(300)
    c2 = client.ouvrir_compte(300)

    c1.retirer(100)

    assert c1.solde == 200
    assert c2.solde == 300

#Un client sans compte est valide (0..1)
def test_client_sans_compte_est_valide():
    client = Client("Hamza")

    assert client.comptes == []


