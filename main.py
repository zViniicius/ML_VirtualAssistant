import argparse
import asyncio
import os

from services.assistant import VoiceAssistant

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

parser = argparse.ArgumentParser(description="Voice Assistant")
parser.add_argument("--language", "-L", type=str, default="pt-BR", help="Linguagem para reconhecimento de voz: (disponível: pt-BR, en-US, es-ES, fr-FR, de-DE, it-IT)")
parser.add_argument("--timeout", "-T", type=int, default=5, help="Tempo limite para reconhecimento de voz (padrão: 5 segundos)")
parser.add_argument("--welcome", "-W", action="store_true", default=False, help="Reproduzir mensagem de boas-vindas")
args = parser.parse_args()

async def main():
    if args.language not in ["pt-BR", "en-US", "es-ES", "fr-FR", "de-DE", "it-IT"]:
        print("Linguagem inválida. Escolha uma das seguintes opções: pt-BR, en-US, es-ES, fr-FR, de-DE, it-IT")
        return
    await VoiceAssistant(language=args.language, timeout=args.timeout, welcome=args.welcome).start()

if __name__ == "__main__":
    asyncio.run(main())