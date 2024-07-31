import datetime

from send_msg import Send_msg


class User_scheduler:

    def __init__(self):
        self.number = input(
            "Digite o número do telefone (com o código do país e DDD,  por exemplo, +5511999999999 para Brasil): "
        )
        self.array_schedule = []
        self.normalize_schedule = []
        self.quit = False
        self._add_new_schedule()
        self.schedule_control = 0

        self.send_msg = Send_msg(self.number)

    def _add_new_schedule(self):

        while self.quit == False:
            schedule_time = input(
                "Digite quando gostaria de enviar a mensagem para o contato (ex: 15h05 ou 09h22) ou Q para sair: "
            )

            if schedule_time:
                if schedule_time == "q" or schedule_time == "Q":
                    self.quit = True
                    self._normalize_schedule_array()
                    break

                self.array_schedule.append(schedule_time)

    def _normalize_schedule_array(self):
        new_array = []
        array_without_h = []

        if self.array_schedule:
            for time in self.array_schedule:

                if "h" in time:
                    array_without_h.append(time.replace("h", ""))

                if "H" in time:
                    array_without_h.append(time.replace("H", ""))

            for time in array_without_h:
                if len(time) == 4:
                    new_array.append((time[:2], time[2:]))

            self.normalize_schedule = new_array

    def schedule_message(self):

        date = datetime.datetime.now()
        date_hour = date.hour
        date_minute = date.minute

        for schecule in self.normalize_schedule:
            if date_hour == int(schecule[0]) and date_minute == int(schecule[1]):
                self.send_msg._send_whatsapp_message(int(schecule[0]), int(schecule[1]))
                self.schedule_control += 1
