class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start alien invasion in an inactive state. 
		self.game_active = False 

		# Hight socre should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics."""
		self.ships_left = self.settings.ship_limit
		self.score = 0

		