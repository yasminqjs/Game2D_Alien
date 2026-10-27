from __future__ import annotations
import pygame
from tests.doubles import StubSemDesconto, StubAlienQueTocouBorda
from pedido import Pedido
from managers.fleet_manager import FleetManager
from config.settings import Settings
from entities.ship import Ship


def test_pedido_com_stub() -> None:
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_fleet_manager_inverte_direcao_com_stub_alien() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)
    fleet_manager = FleetManager(screen, settings, ship)

    stub_alien = StubAlienQueTocouBorda()
    fleet_manager.aliens.add(stub_alien)

    direcao_inicial = settings.fleet_direction
    fleet_manager._check_fleet_edges()

    # O stub forçou a colisão com a borda, logo a direção deve ser invertida
    assert settings.fleet_direction == -direcao_inicial
    # E o alienígena deve ter descido fleet_drop_speed (10 pixels)
    assert stub_alien.rect is not None
    assert stub_alien.rect.y == 110


def test_fleet_manager_create_fleet_alien_positions() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    settings = Settings()
    ship = Ship(screen, settings)
    fleet_manager = FleetManager(screen, settings, ship)
    fleet_manager.create_fleet()

    aliens_list = list(fleet_manager.aliens)
    assert len(aliens_list) > 1
    # Garante que os alienígenas não colapsem na mesma coordenada x
    assert aliens_list[0].rect.x != aliens_list[1].rect.x
    fleet_manager.aliens.update()
    assert aliens_list[0].rect.x != aliens_list[1].rect.x
