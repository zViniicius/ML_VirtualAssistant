# Assistente Virtual ML

## Visão Geral
O Assistente Virtual ML é um assistente ativado por voz que pode realizar várias tarefas, como pesquisar no Google, Wikipedia, abrir o YouTube e encontrar a farmácia mais próxima. Ele suporta vários idiomas e usa reconhecimento de fala para processar comandos.

## Funcionalidades
- Reconhecimento de voz e processamento de comandos
- Suporte multilíngue (pt-BR, en-US, es-ES, fr-FR, de-DE, it-IT)
- Integração com Google, Wikipedia, YouTube e Google Maps
- Respostas em texto para fala

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/zViniicius/ML_VirtualAssistant.git
    cd ML_VirtualAssistant
    ```
2. Instale os pacotes obrigatórios:

   2.1. Usuários Linux
    ```sh
    sudo apt-get install portaudio19-dev python3-pyaudio
    ```
   2.2. Usuários MACOS:
    ```sh
    brew install portaudio
    pip install pyaudio
    ```
3. Crie um ambiente virtual:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # No Windows use `.venv\Scripts\activate`
    ```

4. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script principal:
    ```sh
    python main.py -L pt-BR
    ```
   Substitua `<código_do_idioma>` por um dos códigos de idioma suportados (por exemplo, `en-US`, `pt-BR`).

## Configuração

O dicionário `Translations` em `services/configs.py` contém as mensagens para diferentes idiomas. Você pode adicionar ou modificar traduções conforme necessário.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação.
- `services/assistant.py`: Contém a classe `VoiceAssistant` que lida com a funcionalidade principal.
- `services/configs.py`: Contém o dicionário `Translations` para suporte multilíngue.
- `services/processor.py`: Processa comandos de voz e executa ações correspondentes.
- `services/speech.py`: Lida com a conversão de texto para fala e reprodução de som.
- `utils/__init__.py`: Funções utilitárias, incluindo reconhecimento de fala e inicialização do pygame.

## Comandos de Exemplo

- **Pesquisa no Google**: "siri google" ou "siri pesquisar google"
- **Pesquisa na Wikipedia**: "siri wikipedia" ou "siri pesquisar wikipedia"
- **Abrir YouTube**: "siri youtube" ou "siri abrir youtube"
- **Encontrar Farmácia Mais Próxima**: "siri farmácia" ou "siri encontrar farmácia"
- **Encerrar Assistente**: "siri sair" ou "siri encerrar"

## Contribuição

1. Faça um fork do repositório.
2. Crie um novo branch (`git checkout -b feature-branch`).
3. Faça suas alterações e commit (`git commit -m 'Adicionar nova funcionalidade'`).
4. Faça o push para o branch (`git push origin feature-branch`).
5. Abra um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.