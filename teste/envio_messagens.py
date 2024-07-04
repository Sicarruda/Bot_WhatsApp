import pywhatkit as kit # type: ignore
# import schedule
import time

import pyautogui # type: ignore

# Função para enviar a mensagem
def send_whatsapp_message():
    phone_number = "+5516997750564"  # Substitua pelo número de telefone desejado
    message = "Falei que iria ficar feliz com o que eu fiz"
    hour = 17  # Hora em que a mensagem será enviada (24h)
    minute = 3 # Minuto em que a mensagem será enviada
    
    kit.sendwhatmsg(phone_number, message, hour, minute)
    
    time.sleep(2)
    pyautogui.press('enter')


# Agendar a mensagem para ser enviada em horários fixos
# schedule.every().day.at("16:00").do(send_whatsapp_message)  # Substitua pelo horário desejado

# Loop para manter o script rodando e verificar os agendamentos
# while True:
#     schedule.run_pending()
#     time.sleep(1)







send_whatsapp_message()