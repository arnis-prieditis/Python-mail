# converts lines from zinas.txt to a json list zinas.json
import os
import json

proj_dir = os.path.dirname(os.path.abspath(__file__))
zinas_txt_path = proj_dir + "/zinas.txt"
zinas_json_path = proj_dir + "/zinas.json"

list_of_dict = []

with open(zinas_txt_path, "r") as txt_file:
    for line in txt_file:
        if line.strip() != "":
            list_of_dict.append({"text": line.strip(), "used": 0})

with open(zinas_json_path, "w") as json_file:
    json.dump(list_of_dict, json_file)
