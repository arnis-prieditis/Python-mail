try:
	import json #json faila apstradei
	import random

	import smtplib, ssl #epasta sutisanai

	#mainigie epasta lietam
	port = 465  # For SSL

	smtp_server = "smtp.gmail.com"
	sender_email = "vards.uzvards.69420@gmail.com"  # Enter your address
	receiver_email = "arnis.prieditis19@gmail.com"  # Enter receiver address

	#atver un ielade sarakstu ar novelejumiem
	f = open('/home/arnis/Python-mail/insults.json', 'r')
	insults = json.load(f)
	f.close()

	print("atvera json failu")

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
		print(saturs)

		#zinas nosutisana ar smtplib un ssl
		parole = 'wfsfltjdgnrtbtdn' #app password
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, parole)
			server.sendmail(sender_email, receiver_email, saturs)

		#nomaina izlietotas zinas statusu ('used':0 -> 'used':1) un ieraksta to json failaa
		insults[pos]['used'] = 1
		f = open('/home/arnis/Python-mail/insults.json', 'w')
		json.dump(insults, f)
		f.close()
except Exception as e:
	print(e)
finally:
	print("tika lidz beigam")
