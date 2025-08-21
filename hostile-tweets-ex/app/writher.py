import json

class Writer:
    @ staticmethod
    def write(txt):
        with open('../results/results.json', 'w') as f:
            json.dump(txt, f)