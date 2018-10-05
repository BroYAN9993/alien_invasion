import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """
        Initialize the ship and set inital position.
        """
        self.sreen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get it's enclosing rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Put every new ship on bottom center of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store little values in center attributes of ship.
        self.center = float(self.rect.centerx)

        #Movement sign.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """
        Adjust the position of the ship according to the movement sign.
        """
        #Update center value of ship, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update rect object according to self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """
        Drawn the ship at the specified location.
        """
        self.sreen.blit(self.image, self.rect)
