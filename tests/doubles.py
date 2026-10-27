from __future__ import annotations
import pygame
from desconto import Desconto

IDesconto = Desconto


class StubSemDesconto(Desconto):
    def calcular(self, valor: float) -> float:
        return 0.0


class StubAlienQueTocouBorda(pygame.sprite.Sprite):
    """Stub de alienígena do jogo que sempre responde que atingiu a borda."""
    def __init__(self) -> None:
        super().__init__()
        self.rect: pygame.Rect = pygame.Rect(100, 100, 60, 58)

    def check_edges(self) -> bool:
        return True
