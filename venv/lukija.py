import json

with open('tulos.json') as f:
    data = json.load(f)

print(json.dumps(data, indent = 4, sort_keys=True))