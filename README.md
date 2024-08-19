# Bot de WhatsApp

Este é um bot para WhatsApp que envia mensagens de forma automatizada, utilizando as bibliotecas [pywhatkit](https://pypi.org/project/pywhatkit/) e [pyautogui](https://pyautogui.readthedocs.io/en/latest/).

## Pré-requisitos

- Python 3.6 ou superior
- pywhatkit
- pyautogui
## Estrutura do Projeto

    Bot_WhatsApp/
    ├── json_reader.py      # Classe contendo um leitor de json
    ├── bot_whatsapp.py     # Arquivo principal que vai ser usado para executar o projeto
    ├── mensagens.json      # Arquivo com as mensagens que serão enviadas de maneira aleatória
    ├── send_msg.py         # Classe que envia a mensagem
    ├── user_scheduler.py   # Classe que agenda as mensagens e chama send_msg
    └── README.md           # Este arquivo
## Instalação

1. Clone o repositório:

        git clone https://github.com/Sicarruda/Bot_WhatsApp

2. Navegue até o diretório do projeto:
        
        cd Bot_WhatsApp
3. Crie e ative um ambiente virtual (opcional, mas recomendado):

        python -m venv venv
        source venv/bin/activate  # Para Linux/Mac
        venv\Scripts\activate  # Para Windows
4. Instale as dependências:

        pip install -r requirements.txt
Se o arquivo requirements.txt não estiver presente, você pode instalar as bibliotecas diretamente:

    pip install pywhatkit pyautogui

## Como usar

1. Edite o arquivo mensagens.json para incluir as mensagens que deseja enviar:

Exemplo de mensagens.json:

    [
        "Olá! Como você está?",
        "Não se esqueça da nossa reunião às 15h.",
        "Bom dia! Tenha um ótimo dia!"
    ]

2. Execute o bot:
        
        python3 bot_whatsapp.py

3. Insira os dados solicitados:
- Número de telefone (com o código do país e DDD, por exemplo, +5511999999999 para Brasil):
    
      Digite o número do telefone (com o código do país e DDD, por exemplo, +5511999999999 para Brasil): 

- Horário de envio da mensagem, lembrando que é possivel agendar n horários desde que sejam no mesmo dia:

      Digite quando gostaria de enviar a mensagem para o contato (ex: 15h05 ou 09h22) ou Q para sair: 

## Licença

Sinta-se à vontade para ajustar qualquer parte conforme necessário para o seu projeto específico. Se precisar de mais alguma coisa, estou aqui para ajudar!


Este projeto é licenciado sob os termos da [MIT](https://choosealicense.com/licenses/mit/)


