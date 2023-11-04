#vel vajag noformet pasas zinas saturu, lai visas rindas aizsuta
import os
import json #json faila apstradei
import random
from datetime import date
import smtplib, ssl #epasta sutisanai
from email.message import EmailMessage

#mainigie epasta lietam
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "vards.uzvards.69420@gmail.com"  # Enter your address
receiver_email = "arnis.prieditis19@gmail.com"  # Enter receiver address: adamovics222@gmail.com

proj_dir = os.path.dirname(os.path.abspath(__file__))
zinu_fails = proj_dir + '/zinas.json' #saraksts ar objektiem {"text": "", "used": 0}

#atver un ielade sarakstu ar novelejumiem
with open(zinu_fails, 'r') as f:
	insults = json.load(f)

#lai parbauditu, vai ir vel neaizsutiti velejumi
unused = filter(lambda elem: elem['used'] == 0, insults)

if(len(list(unused)) == 0):
	print('Vajag jaunus novelejumus')
else:
	#dabu poziciju vienam no vel neizmantotajiem
	pos = random.randint(0, len(insults)-1)
	while insults[pos]['used'] == 1:
		pos = random.randint(0, len(insults)-1)

	#ieliek zinas saturu mainigaja
	saturs = insults[pos]['text']
	log_file_path = proj_dir + '/sent.log'
	with open(log_file_path, 'a') as log:
		log.write(f"Date: {date.today()}\n")
		log.write(f"Ziņa: {saturs}\n\n")

	# zinas noformesana
	msg = EmailMessage()
	msg['Subject'] = 'Tavs Iknedēļas Vēstnesis'
	msg['From'] = sender_email
	msg['To'] = receiver_email
	msg.set_content(saturs)

	#zinas nosutisana ar smtplib un ssl
	parole = 'wfsfltjdgnrtbtdn' #app password
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, parole)
		server.send_message(msg)

	#nomaina izlietotas zinas statusu ('used':0 -> 'used':1) un ieraksta visu atpakal json failaa
	insults[pos]['used'] = 1
	with open(zinu_fails, 'w') as f:
		json.dump(insults, f)
