import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to mange bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet obejct at the ship's locaation"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correction postition
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's postition as a decimal vaule
        self.y = float(self.rect.y)

    def update(self):
        """MOve the bullet up the screen"""
        # Update the decimal postition of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect postition
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)