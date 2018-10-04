import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    """
    Initialize pygame, settings and screen object.
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #Create a ship.
    ship = Ship(screen)

    #Set a background colour.
    bg_color = (230, 230, 230)

    #Start the main cycle of the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()