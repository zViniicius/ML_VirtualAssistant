import asyncio
import threading

from services.configs import Translations
from services.speech import text_to_speech, play_sound
from services.processor import process_command
from utils import initialize_pygame, recognize_speech

class VoiceAssistant:
    """
    Classe que implementa um assistente de voz, capaz de ouvir comandos e responder
    de forma interativa. Utiliza APIs para conversão de texto para fala, reconhecimento de
    voz e execução de comandos.

    Attributes:
        language (str): O idioma utilizado para a interação do assistente.
        timeout (int): O tempo máximo de espera para comandos em segundos.
        is_listening (bool): Indica se o assistente está escutando comandos.
        speech_lock (threading.Lock): Lock para controle da concorrência no processamento de fala.
    """

    def __init__(self, language="pt-BR", timeout=5,welcome=True):
        """
        Inicializa o assistente de voz com o idioma e o timeout configurados.

        Parameters:
            language (str): O idioma utilizado pelo assistente. O padrão é "pt-BR".
            timeout (int): O tempo máximo de espera para comandos, em segundos. O padrão é 5.
        """
        self.language = language
        self.timeout = timeout
        self.play_welcome = welcome
        self.is_listening = False
        self.speech_lock = threading.Lock()

    @staticmethod
    async def initialize_system():
        """
        Inicializa o sistema, incluindo a biblioteca Pygame.

        Esta função é chamada no início da execução do assistente para preparar o ambiente.
        """
        print("Inicializando o sistema...")
        await initialize_pygame()

    async def start(self):
        """
        Inicia o assistente de voz, realizando a inicialização do sistema e começando a escutar
        comandos de voz.

        A função também reproduz uma mensagem de boas-vindas no idioma configurado.
        """
        await self.initialize_system()
        await text_to_speech(Translations[self.language]["WELCOME_MESSAGE"]) if self.play_welcome else None
        self.is_listening = True
        print("Assistente de voz iniciado.")
        await self.listen()

    async def listen(self):
        """
        Fica em loop aguardando por comandos de voz. Quando um comando é detectado, ele é
        processado. Comandos que começam com "siri" são tratados, e uma resposta é dada
        dependendo se o comando foi reconhecido ou não.

        Durante o processamento do comando, o assistente não escuta novos comandos até
        a execução ser concluída.
        """
        while True:
            if self.is_listening:
                command = await self.speech_to_text()
                if command and command.startswith("siri"):
                    command = command.replace("siri", "").strip()
                    if command:
                        await play_sound()
                        self.is_listening = False
                        await process_command(self, command)
                        await asyncio.sleep(0.5)
                        self.is_listening = True
                    else:
                        await play_sound()
                        await text_to_speech(Translations[self.language]["RETRY_MESSAGE"])
            await asyncio.sleep(0.5)

    async def speech_to_text(self):
        """
        Realiza o reconhecimento de fala e converte o áudio em texto.

        Returns:
            str: O comando reconhecido a partir da fala.
        """
        return await recognize_speech(self.language)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    asyncio.run(assistant.start())
