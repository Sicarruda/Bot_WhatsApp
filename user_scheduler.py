import datetime

from send_msg import Send_msg


class User_scheduler:

    def __init__(self):
        self.number = input(
            "Digite o número do telefone (com o código do país e DDD,  por exemplo, +5511999999999 para Brasil): "
        )
        self.array_schedule = []
        self.quit = False
        self._add_new_schedule()

        self.send_msg = Send_msg(self.number)
        self.send_whatsapp = self.send_msg._send_whatsapp_message

    def _add_new_schedule(self):

        while self.quit == False:
            schedule_time = input(
                "Digite quando gostaria de enviar a mensagem para o contato (ex: 15h05 ou 09h22) ou Q para sair: "
            )

            if schedule_time:
                if schedule_time == "q" or schedule_time == "Q":
                    self.quit = True
                    break

                self.array_schedule.append(schedule_time)

    def _normalize_schedule_array(self):
        new_array = []
        
        if self.array_schedule:
            for time in self.array_schedule:

                if "h" in time:
                    time.replace("h", "")

                if "H" in time:
                    time.replace("H", "")

            for time in self.array_schedule:
                if len(time) == 4:
                    new_array.append((time[:1], time[2:]))

            return new_array

    def schedule_message(self):
        # schedule_time = [(hora, minuto)]
        schedule_time = self._normalize_schedule_array()
        date = datetime.datetime.now()
        date_hour = date.hour
        date_minute = date.minute

        for schecule in schedule_time:
            if date_hour == schecule[0] and date_minute == schecule[1]:
                self.send_whatsapp(schecule[0], schecule[1])
