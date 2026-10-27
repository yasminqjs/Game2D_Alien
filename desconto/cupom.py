from abc import ABC, abstractmethod


class Cupom(ABC):
    @abstractmethod
    def aplicar(self, codigo: str) -> bool:
        pass


class CupomVIP(Cupom):
    def aplicar(self, codigo: str) -> bool:
        return codigo == "DESC10"