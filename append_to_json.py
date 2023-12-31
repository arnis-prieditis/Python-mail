# appends lines in file new_zinas.txt to the json list in zinas.json
import os
import json

proj_dir = os.path.dirname(os.path.abspath(__file__))
new_zinas_txt_path = proj_dir + "/new_zinas.txt"
zinas_json_path = proj_dir + "/zinas.json"

with open(zinas_json_path, 'r') as f:
	zinu_saraksts = json.load(f)


with open(new_zinas_txt_path, "r") as txt_file:
    for line in txt_file:
        if line.strip() != "":
            zinu_saraksts.append({"text": line.strip(), "used": 0})

with open(zinas_json_path, "w") as json_file:
    json.dump(zinu_saraksts, json_file, indent=4)
