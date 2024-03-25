from note import Note
from note import Key
import pygame
from names import note_names


def get_notes() -> list[Note]:  # lista nutek
    notes = []
    for name in note_names:
        # randomowy dzwiek zeby sie kompilowalo
        note = Note(name, pygame.mixer.Sound('moai.wav'))
        notes.append(note)
        if name == 'C':
            pygame.mixer.Sound.play(note.sound)
    for name in note_names:
        note = Note(name, pygame.mixer.Sound('moai.wav'))
        notes.append(note)
    return notes


# lista klawiszy w kolejnosci takiej jaka jest na klawiaturze
def draw_piano(screen: pygame.Surface, notes: list[Note], margines=(100, 100)) -> list[Key]:

    keys = []
    height = screen.get_height()
    width = screen.get_width()
    white_height = height - 2*margines[1]
    white_width = (width-2*margines[0])/14
    black_height = 2/3*white_height
    black_width = 3/5*white_width

    LAYER_WHITE = pygame.Surface((width, height))
    LAYER_WHITE = LAYER_WHITE.convert_alpha()
    LAYER_WHITE.fill((0, 0, 0, 0))

    LAYER_BLACK = pygame.Surface((width, height))
    LAYER_BLACK = LAYER_BLACK.convert_alpha()
    LAYER_BLACK.fill((0, 0, 0, 0))

    white_counter = 0

    for note in notes:
        if note.black:
            rect = pygame.draw.rect(LAYER_BLACK, 'black', pygame.Rect(
                margines[0]+(white_counter-1/3)*white_width, margines[1], black_width, black_height), 0, 2)
            keys.append(Key(note, rect))
        else:
            rect = pygame.draw.rect(
                LAYER_WHITE, 'white', pygame.Rect(margines[0]+white_counter*white_width, margines[1], white_width, white_height), 0, 2)
            pygame.draw.rect(
                LAYER_WHITE, 'black', pygame.Rect(margines[0]+white_counter*white_width, margines[1], white_width, white_height), 2, 2)
            white_counter += 1
            keys.append(Key(note, rect))

    screen.blit(LAYER_WHITE, (0, 0))
    screen.blit(LAYER_BLACK, (0, 0))

    return keys
