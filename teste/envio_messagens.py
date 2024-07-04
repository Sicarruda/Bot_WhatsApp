import pywhatkit as kit # type: ignore
import schedule # type: ignore
import pyautogui # type: ignore
import time
import datetime
import json
import random


def randon_msg(msg_json):
    with open(msg_json, 'r') as file:
        data = json.load(file)

    msgs = data["msg"]

    return random.choice(msgs)

def close_whatsapp():
    pass

# Função para enviar a mensagem
def send_whatsapp_message(phone_number, message, hour, minute):  
    kit.sendwhatmsg(phone_number, message, hour, minute)
    time.sleep(2)
    pyautogui.press('enter')

    close_whatsapp()

def schedule_message():
    date = datetime.datetime.now()
    phone_number = "+5516997750564"  # Substitua pelo número de telefone desejado  
    message = f"{randon_msg('teste/messagens.json')} P.S. Desliga o meu PC"
    hour = date.hour
    minute = date.minute + 1
    send_whatsapp_message(phone_number,message,hour,minute)

    # if hour >= 0 and hour < 3 :
    #     send_whatsapp_message(phone_number,message,hour,minute)

# Loop para manter o script rodando e verificar os agendamentos
# while True:
#     schedule_message()
#     time.sleep(1800)

schedule_message()