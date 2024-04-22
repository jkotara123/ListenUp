import pygame
import wave


class Sound:
    def __init__(self, note_name) -> None:
        file_path = "soundFiles\\"+note_name+".wav"
        self.sound: pygame.mixer.Sound = pygame.mixer.Sound(file_path)
        self.duration: float = get_wav_duration(file_path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)


def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # Get the number of frames and the frame rate (frames per second)
        num_frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()

        # Calculate the duration in seconds
        duration = num_frames / frame_rate

        return duration
