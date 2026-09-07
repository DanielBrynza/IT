import json

# Чтение файла в Python:
with open("config.json", "r") as file:
    config = json.load(file)

# Теперь config — это обычный словарь Python!
print(config.get("environment"))