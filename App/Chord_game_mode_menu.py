from Game_mode_menu import GameModeMenu


class ChordGameModeMenu(GameModeMenu):
    def __init__(self, root=None, launch_immediately=True, octaves=2, lowest_octave=2, game_mode_specs=None):
        super().__init__(root=root, launch_immediately=launch_immediately, octaves=octaves,
                         lowest_octave=lowest_octave, game_mode_prompt="Chord", game_mode_specs=game_mode_specs)
