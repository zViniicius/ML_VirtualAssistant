import webbrowser
import difflib

from services.configs import Translations
from services.speech import text_to_speech

COMMANDS = {
    "google": ["google", "pesquisar google", "pesquisar", "pesquisar na internet"],
    "wikipedia": ["wikipedia", "pesquisar wikipedia"],
    "youtube": ["youtube", "abrir youtube", "assistir", "vídeos", "músicas", "entretenimento"],
    "farmácia": ["farmácia", "encontrar farmácia", "farmácia próxima", "remédios", "medicamentos"],
    "sair": ["sair", "encerrar", "fechar"]
}


async def process_command(instance, command):
    """
    Processa o comando de voz reconhecido e executa a ação correspondente.

    Este método encontra o comando mais próximo a partir do comando de voz fornecido e chama a função
    que executa a ação relacionada ao comando.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
        command (str): Comando de voz reconhecido.

    """
    matched_command = find_closest_command(command)
    if matched_command:
        await execute_command(instance, matched_command)
    else:
        await text_to_speech(Translations[instance.language]["UNKNOWN_COMMAND"])


def find_closest_command(command):
    """
    Encontra o comando mais próximo baseado em similaridade utilizando a função `difflib.get_close_matches`.

    Esta função compara o comando de voz fornecido com os possíveis comandos definidos em `COMMANDS`
    e retorna o comando mais similar encontrado.

    Parameters:
        command (str): Comando de voz reconhecido.

    Returns:
        str: O comando correspondente encontrado na lista de possíveis comandos, ou `None` se não houver
             correspondência suficiente.
    """
    command = command.lower()
    for action, possible_commands in COMMANDS.items():
        matches = difflib.get_close_matches(command, possible_commands, n=1, cutoff=0.6)
        if matches:
            return action
    return None


async def execute_command(instance, command):
    """
    Executa o comando correspondente com base na ação encontrada.

    Para cada comando identificado, chama a função específica que executa a ação associada.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
        command (str): Comando correspondente a ser executado.
    """
    commands = {
        "google": search_google,
        "wikipedia": search_wikipedia,
        "youtube": open_youtube,
        "farmácia": find_nearest_pharmacy,
        "sair": exit_assistant
    }
    await commands[command](instance)


async def search_google(instance):
    """
    Realiza uma pesquisa no Google com base no termo fornecido pelo usuário.

    O assistente solicita ao usuário que diga o termo para pesquisa, em seguida, abre o Google com a pesquisa
    e comunica o usuário sobre o resultado.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
    """
    await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["google"]["search"])
    term = await instance.speech_to_text()
    if term:
        webbrowser.open(f"https://www.google.com/search?q={term.replace(' ', '+')}")
        await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["google"]["result"].format(term=term))


async def search_wikipedia(instance):
    """
    Realiza uma pesquisa na Wikipedia com base no termo fornecido pelo usuário.

    O assistente solicita ao usuário que diga o termo para pesquisa, em seguida, abre a Wikipedia com o artigo
    correspondente e comunica o usuário sobre o resultado.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
    """
    await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["wikipedia"]["search"])
    term = await instance.speech_to_text()
    if term:
        webbrowser.open(f"https://pt.wikipedia.org/wiki/{term.replace(' ', '_')}")
        await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["wikipedia"]["result"].format(term=term))


async def open_youtube(instance):
    """
    Abre o site do YouTube.

    Esta função simplesmente abre o YouTube no navegador e avisa o usuário.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
    """
    webbrowser.open("https://www.youtube.com")
    await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["youtube"])


async def find_nearest_pharmacy(instance):
    """
    Abre uma pesquisa no Google Maps para encontrar farmácias próximas.

    Esta função solicita ao usuário que procure farmácias na sua área e abre o Google Maps com a pesquisa.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
    """
    webbrowser.open("https://www.google.com/maps/search/farmácia+próxima/")
    await text_to_speech(Translations[instance.language]["COMMAND_MESSAGES"]["farmácia"])


async def exit_assistant(instance):
    """
    Encerra o assistente de voz.

    Este comando encerra a execução do assistente de voz e comunica a despedida ao usuário.

    Parameters:
        instance (VoiceAssistant): Instância do assistente de voz.
    """
    await text_to_speech(Translations[instance.language]["GOODBYE_MESSAGE"])
    exit()
