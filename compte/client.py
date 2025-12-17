from dataclasses import dataclass
from typing import Optional
from compte.compte_bancaire import CompteBancaire

@dataclass
class Client:
    nom: str
    compte: Optional[CompteBancaire] = None #Optional[CompteBancaire] soit il a un compte soit non 0..1

    def ouvrir_compte(self, solde_initial: float = 0.0):
        self.compte = CompteBancaire(self.nom, solde_initial)