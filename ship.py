import pygame

class Ship():

    def __init__(self, screen):
        """
        Initialize the ship and set inital position.
        """
        self.sreen = screen

        #Load the ship image and get it's enclosing rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.sreen_rect = screen.get_rect()

        #Put every new ship on bottom center of screen.
        self.rect.centerx = self.sreen_rect.centerx
        self.rect.bottom = self.sreen_rect.bottom

        #Movement sign.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """
        Adjust the position of the ship according to the movement sign.
        """
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """
        Drawn the ship at the specified location.
        """
        self.sreen.blit(self.image, self.rect)
