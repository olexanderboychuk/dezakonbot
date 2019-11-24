import json

with open("conf.json", 'r') as f:
    configuration = json.loads(f.read())