import os
import json

proj_dir = os.path.dirname(os.path.abspath(__file__))
zinu_fails = proj_dir + '/zinas.json' #saraksts ar objektiem {"text": "", "used": 0}

#atver un ielade sarakstu ar novelejumiem
with open(zinu_fails, 'r') as f:
	insults = json.load(f)

#izfiltre neizmantotos
unused = filter(lambda elem: elem['used'] == 0, insults)

print(f"{len(list(unused))} no {len(list(insults))}")