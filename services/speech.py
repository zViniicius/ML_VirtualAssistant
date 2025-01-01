import pyttsx3
import pygame
from asyncio import sleep

from assets import END_SOUND_FILE, START_SOUND_FILE

engine = pyttsx3.init()

async def text_to_speech(text):
    """
    Converte o texto em fala usando a biblioteca pyttsx3.

    Este método usa o motor de texto-para-fala pyttsx3 para converter o texto fornecido em fala
    e aguarda até que a fala seja completamente pronunciada.

    Parameters:
        text (str): O texto a ser convertido em fala.

    Returns:
        None
    """
    engine.say(text)
    engine.runAndWait()

async def play_sound(is_start=True):
    """
    Toca um som de confirmação.

    Este método usa o Pygame para carregar e tocar um som de confirmação. O som que será tocado
    depende do parâmetro `is_start`. Se `is_start` for `True`, o som de início será tocado; caso
    contrário, o som de fim será tocado.

    Parameters:
        is_start (bool): Determina se o som a ser tocado é de início ou fim.
                         O padrão é `True` (som de início).

    Returns:
        None
    """
    pygame.mixer.music.load(START_SOUND_FILE if is_start else END_SOUND_FILE)
    pygame.mixer.music.play()
    await sleep(1)
