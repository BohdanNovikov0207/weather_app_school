import os, json

# loeb fail mis on kirjutatud
def read(file_name: str):
    # vastutab funktsiooniparameetris määratud faili tee genereerimise eest ja salvestab selle muutujasse
    path = os.path.abspath(__file__ + '/../../static/' + file_name)
    # avab fail teel mis on määratud path`is ja tagastab file mis on töödeldus sõnastikuna
    with open(path, encoding= "utf-8") as file:
        return json.load(file)
    