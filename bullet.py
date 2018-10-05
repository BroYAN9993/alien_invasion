import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    A class for managing shotting bullets.
    """
    def __init__(self, ai_settings, screen, ship):
        """
        Create a bullet object in the position where the ship locates.
        """
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a rectangle in spot (0, 0) which representing a bullet.
        #Then move it to right position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store bullet position expressed in decimals.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        Move the bullets up.
        """
        #Update decimal values which expressing bullet position.
        self.y -= self.speed_factor
        #Update rect position which expressing bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw bullets on screen.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
