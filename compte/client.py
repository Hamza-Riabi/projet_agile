from dataclasses import dataclass, field
from typing import Optional
from compte.compte_bancaire import CompteBancaire

@dataclass
class Client:
    nom: str
    comptes: List[CompteBancaire] = field(default_factory=list)
    #0..1
    compte: Optional[CompteBancaire] = None #Optional[CompteBancaire] soit il a un compte soit non 0..1

    def ouvrir_compte(self, solde_initial: float = 0.0) -> CompteBancaire:
        compte = CompteBancaire(titulaire=self, solde=solde_initial)
        self.comptes.append(compte)
        return compte