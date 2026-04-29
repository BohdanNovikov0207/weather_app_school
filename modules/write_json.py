import json, os

# first we create function and parameters, then we set path to file and edit file on this path
def write(file_name: str, data: dict):
    path = os.path.abspath(__file__ + f"/../../static/{file_name}")
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)