from __future__ import annotations
from typing import Any
import pygame
from pygame.surface import Surface

from config.settings import Settings
from entities.bullet import Bullet
from entities.ship import Ship


class BulletManager:
    """Responsável apenas por criar, atualizar e desenhar os projéteis."""

    def __init__(self, screen: Surface, settings: Settings, ship: Ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets: pygame.sprite.Group[Any] = pygame.sprite.Group()

    def fire_bullet(self) -> None:
        """Dispara um projétil se o limite de projéteis ainda não tiver sido alcançado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    # Alias para compatibilidade com testes unitários
    _fire_bullet = fire_bullet

    def update_bullets(self, aliens: Any) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
        self.bullets.update()
        self.remove_offscreen_bullets()
        self.check_bullet_alien_collisions(aliens)

    def remove_offscreen_bullets(self) -> None:
        """Remove os projéteis que saíram da tela."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def check_bullet_alien_collisions(self, aliens: Any) -> None:
        """Verifica colisões entre projéteis e alienígenas."""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)
