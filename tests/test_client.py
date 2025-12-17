from compte.client import Client
#Test avec fixture (setup) 
def test_client_ouvre_un_compte():
    client = Client("Hamza")
    client.ouvrir_compte(200)

    assert client.compte is not None
    assert client.compte.solde == 200
