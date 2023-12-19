#vel vajag noformet pasas zinas saturu, lai visas rindas aizsuta
import os
import json #json faila apstradei
import random
from datetime import date
import smtplib, ssl #epasta sutisanai
from email.message import EmailMessage
from email.utils import make_msgid

#mainigie epasta lietam
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "vards.uzvards.69420@gmail.com"
receiver_email = ""
proj_dir = os.path.dirname(os.path.abspath(__file__))

#atver un ielade sarakstu ar novelejumiem
path_to_zinas = proj_dir + '/zinas.json' #saraksts ar objektiem {"text": "", "used": 0}
with open(path_to_zinas, 'r') as f:
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

	# lai piefiksetu aizsutito
	log_file_path = proj_dir + '/sent.log'
	with open(log_file_path, 'a') as log:
		log.write(f"Date: {date.today()}\n")
		log.write(f"Ziņa: {saturs}\n\n")

	# zinas noformesana
	msg = EmailMessage()
	msg['Subject'] = 'Tavs Iknedēļas Vēstnesis'
	msg['From'] = sender_email
	msg['To'] = receiver_email

	# vajag citadak apstradat, ja ir bilde klat zinai
	if ":/images/" in saturs:
		msg_with_image = saturs.split(":")
		msg.set_content(msg_with_image[0])

		# Add the html version.  This converts the message into a multipart/alternative
		# container, with the original text message as the first part and the new html
		# message as the second part.
		img_cid = make_msgid()
		msg.add_alternative("""\
		<html>
		<head></head>
		<body>
			<p>{text}</p>
			<img src="cid:{img_cid}" />
		</body>
		</html>
		""".format(text=msg_with_image[0], img_cid=img_cid[1:-1]), subtype='html')
		# note that we needed to peel the <> off the msgid for use in the html.

		# Now add the related image to the html part.
		path_to_img = proj_dir + msg_with_image[1]
		with open(path_to_img, 'rb') as img:
			msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid=img_cid)
	else:
		msg.set_content(saturs)

	#zinas nosutisana ar smtplib un ssl
	parole = "" # app password is read from file
	path_to_parole = proj_dir + "/parole.txt"
	with open(path_to_parole, "r") as pswd_file:
		parole = pswd_file.readline()
		parole.strip()
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, parole)
		server.send_message(msg)

	#nomaina izlietotas zinas statusu ('used':0 -> 'used':1) un ieraksta visu atpakal json failaa
	insults[pos]['used'] = 1
	with open(path_to_zinas, 'w') as f:
		json.dump(insults, f)
