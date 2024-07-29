import datetime

from send_msg import Send_msg

class User_scheduler():

    def __init__(self):
        self.send_msg = Send_msg("5516997750564")
        self.send_whatsapp = self.send_msg._send_whatsapp_message
        
    def schedule_message(self, schedule_time):
    # schedule_time = [(hora, minuto)]
        date = datetime.datetime.now()
        date_hour = date.hour
        date_minute = date.minute

        for schecule in schedule_time:
            if date_hour == schecule[0] and date_minute == schecule[1]:
                self.send_whatsapp(schecule[0], schecule[1])

    