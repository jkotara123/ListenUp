from Game_mode_menu import GameModeMenu


class IntervalGameModeMenu(GameModeMenu):
    def __init__(self, root=None, launch_immediately=True, octaves=2, lowest_octave=2):
        super().__init__(root=root, launch_immediately=launch_immediately, octaves=octaves, lowest_octave=lowest_octave, game_mode_prompt="Interval")
