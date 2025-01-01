import speech_recognition as sr
import pygame

from services.configs import Translations
async def initialize_pygame():
    """
    Inicializa o mixer de som do Pygame de forma assíncrona.

    Este método prepara o Pygame para reprodução de sons. A inicialização ocorre de forma assíncrona.

    Returns:
        None
    """
    pygame.mixer.init()

async def recognize_speech(language="pt-BR"):
    """
    Converte fala em texto usando a biblioteca SpeechRecognition.

    Este método utiliza a biblioteca `speech_recognition` para capturar áudio do microfone e
    convertê-lo em texto, usando o Google Web Speech API. O idioma pode ser configurado através
    do parâmetro `language`.

    Parameters:
        language (str): O idioma a ser utilizado para o reconhecimento de fala. O padrão é "pt-BR" (português do Brasil).

    Returns:
        str: O texto reconhecido a partir da fala. Retorna `None` se não conseguir reconhecer a fala ou se ocorrer algum erro.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            response = recognizer.recognize_google(audio, language=language)
            print(Translations[language]["YOU_SAID"].format(response=response))
            return response.lower()
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            return None
