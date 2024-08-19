import pywhatkit as kit
import pyautogui
import time

from json_reader import Json_reader


class Send_msg:
    # Envia mensagens via WhatsApp

    def __init__(self, number):
        self.json_msg = Json_reader()
        self.msg = f"{self.json_msg.json_random_msg()}"
        self.phone_number = number

    def _send_whatsapp_message(self, hour, minute):
        # Envia mensagem pelo WhatsApp web 

        kit.sendwhatmsg(self.phone_number, self.msg, hour, (minute + 1))
        pyautogui.press("enter")
        time.sleep(2) # segundos
        self._close_whatsapp()

    def _close_whatsapp(self):
        # Fecha o navegador

        pyautogui.hotkey('alt', 'f4')
        
