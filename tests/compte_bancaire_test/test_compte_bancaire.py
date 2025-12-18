import pytest
from compte.compte_bancaire import CompteBancaire

def test_depot():
    compte = CompteBancaire("Ali", 100)
    compte.deposer(50)
    assert compte.solde == 150

def test_retrait():
    compte = CompteBancaire("Ali", 100)
    compte.retirer(40)
    assert compte.solde == 60

def test_retrait_solde_insuffisant():
    compte = CompteBancaire("Ali", 50)
    with pytest.raises(ValueError):
        compte.retirer(100)