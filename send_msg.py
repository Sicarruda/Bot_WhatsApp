import pywhatkit as kit
import pyautogui
import time

from json_reader import Json_reader


class Send_msg:

    def __init__(self, number):
        self.json_msg = Json_reader()
        self.msg = f"{self.json_msg.json_random_msg()} P.S. Desliga o meu PC"
        self.phone_number = number

    def _send_whatsapp_message(self, hour, minute):
        kit.sendwhatmsg(self.phone_number, self.msg, hour, (minute + 1))
        time.sleep(1)
        pyautogui.press("enter")
        self._close_whatsapp()

    def _close_whatsapp(self):
        pass
