from dataclasses import dataclass

@dataclass
class CompteBancaire:
    titulaire: str
    solde: float = 0.0

    def deposer(self, montant: float) -> None:
        if montant <= 0:
            raise ValueError("montant invalide")
        self.solde += montant

    def retirer(self, montant: float) -> None:
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self.solde:
            raise ValueError("solde insuffisant")
        self.solde -= montant
#ajouter get et set (@property)
#techniques de factoring :
#Rename retirer-->deviter
#ExtractMethod :def _verifier_montant(self, montant: float):
                 # if montant <= 0:
                 #  raise ValueError("Montant invalide")



#écrire feature -->steps-->behave                 

#refactoring dans BDD: Mutualisation des steps (retrait et depot dans meme step)

#Le fichier .feature n’exécute rien tout seul.
#C’est Behave qui :

#lit le texte puis reconnaît des phrases et appelle les fonctions Python correspondantes (si je trouve given dans feature , j'appele la fonction given dans steps)



