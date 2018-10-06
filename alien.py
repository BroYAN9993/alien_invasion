import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Class to express single alien.
    """

    def __init__(self, ai_settings, screen):
        """
        Initialize alien and set its starting position.
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every alien is initially near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact position of alien.
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Draw alien at specified position.
        """
        self.screen.blit(self.image, self.rect)
