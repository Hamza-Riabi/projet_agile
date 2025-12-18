from compte.client import Client

def test_client_ouvre_un_compte():
    client = Client("Hamza")
    compte = client.ouvrir_compte(200)

    assert len(client.comptes) == 1
    assert compte.solde == 200
    assert compte.titulaire == client
