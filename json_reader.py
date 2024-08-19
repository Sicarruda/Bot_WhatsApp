import json
import random

class Json_reader():
    # Classe para ler arquivos json
 
    def __init__(self):
        self.json_file = "messagens.json"

    def _reader(self):
        # Le arquivo Json
        
        with open(self.json_file, "r") as file:
            data = json.load(file)

        msgs = data["msg"]

        return msgs

    def json_random_msg(self):
        # Devolve uma linha aleatoria do arquivo

        return random.choice(self._reader())
    