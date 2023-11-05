# Python-mail
Python skripts, kas jauzliek uz kkada servera, ka strādā 24/7, lai reizi nedēļā Andrim uz e-pastu atnāktu kāda jauka ziņa.

## Failu overview
### send_mail.py
Galvenais skripts, kas jāpalaiž, lai nosūtītu e-pastu.

### zinas.json
Fails, no kura tiek ņemtas ziņas, ko sūtīt. Tas ir saraksts no vārdnīcām ar laukiem "text" un "used", lai skripts noteiktu, vai ziņa jau ir lietota. Tas ir jāpārbauda, jo send_mail randomā izvēlas nosūtāmo ziņu.

### sent.log
Log fails, kurā pēc katras ziņas nosūtīšanas ieraksta nosūtīšanas datumu un ziņas tekstu.

### txt_to_json.py un zinas.txt
Skripts un "avots", kas zinas.json failā izveido jaunu sarakstu ar ziņām - visām ziņa=ās statuss "used" ir 0.

### append_to_json.py un new_zinas.txt
Skripts un "avots", no kura pievieno jaunas rindas zinas,json failā, neizmainot statusu jau esošajām ziņām.

## Setup
Šobrīd šis repozitorijs ir pullots uz android telefona, kurā ir ielādēts Termux. Automātiskā, regulārā skripta palaišana tiek nodrošināta ar crontab/cronjob lietu. E-pasts tiek sūtīts katru nedēļu pirmdien 7:00.

## Papildus info
Sūtītāja adrese ir vards.uzvards.69420@gmail.com - dummy epasts, kuram ir izveidota app password, kas ir cieti iekodēta skriptā. Varbūt drošības pēc to vajadzētu glabāt atsevišķā failā, idk.
