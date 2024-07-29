import json
import random

class Json_reader():
 
    def __init__(self):
        self.json_file = "teste/messagens.json"

    def _reader(self):
        with open(self.json_file, "r") as file:
            data = json.load(file)

        msgs = data["msg"]

        return msgs

    def json_random_msg(self):
        return random.choice(self._reader())
    