import pygame
from pygame.sprite import Sprite

class Alien(sprite):
	"""A class to represent a single alien in the fleet"""

	def __init__ (self, ai_game):
		"""Initialise the alien and set it's starting position"""
		super().__init__()
		self.screen = ai_game.screen

		# load the the alien image and set it's rect image.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen. 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the aliens horizontal postion.
		self.x = float(self.rect.x)
