import wave
import json
import pygame

with open('resources/config.json', 'r') as f:
    config = json.load(f)
sound_files_path = config["paths"]["sound_files_path"]


class Sound:
    def __init__(self, note_name) -> None:
        file_path = f"{sound_files_path}/{note_name}.wav"
        self.sound: pygame.mixer.Sound = pygame.mixer.Sound(file_path)
        self.duration: float = get_wav_duration(file_path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)


def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        num_frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()
        duration = num_frames / frame_rate
        return duration
