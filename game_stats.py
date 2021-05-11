class GameStats:
    """Track statisitics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialzie statics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initzsalibes statcis that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1