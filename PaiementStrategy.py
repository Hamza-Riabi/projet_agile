from abc import ABC, abstractmethod

class PaiementStrategy(ABC):

    @abstractmethod
    def payer(self, montant):
        pass
