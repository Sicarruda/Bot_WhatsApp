import time
from user_scheduler import User_scheduler


class Bot_whatsApp:
    def __init__(self):
        self.user_scheduler = User_scheduler()
        self.run = True

    def _check_schedule(self):
        if self.user_scheduler.schedule_control >= len(
            self.user_scheduler.normalize_schedule
        ):
            self.run = False

    def run_schedule(self):

        while self.run:
            self.user_scheduler.schedule_message()
            self._check_schedule()


if __name__ == "__main__":
    bot = Bot_whatsApp()
    bot.run_schedule()
