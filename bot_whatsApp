from user_scheduler import User_scheduler
import time


class Bot_whatsApp:
    # Envia mensagens aleatorias agendadas pelo WhatsApp Web
    def __init__(self):
        self.user_scheduler = User_scheduler()
        self.run = True

    def _check_schedule(self):
        # Verifica se a horarios agendados

        if self.user_scheduler.schedule_control >= len(
            self.user_scheduler.normalize_schedule
        ):
            self.run = False

    def run_schedule(self):
        # Roda o programa
        
        delay_in_s = 30

        while self.run:
            self.user_scheduler.schedule_message()
            self._check_schedule()
            
            time.sleep(delay_in_s)


if __name__ == "__main__":
    bot = Bot_whatsApp()
    bot.run_schedule()
