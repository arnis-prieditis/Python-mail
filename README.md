# Python-mail
Python skripts, kas reizi nedēļā Andrim uz e-pastu atsūta kādu jauku ziņu.

## Failu overview
### send_mail.py
Galvenais skripts, kas jāpalaiž, lai nosūtītu e-pastu.

### zinas.json
Fails, no kura tiek ņemtas ziņas, ko sūtīt. Tas ir saraksts no vārdnīcām 
ar laukiem "text" un "used", lai skripts noteiktu, vai ziņa jau ir bijusi nosūtīta.

### sent.log
Log fails, kurā pēc katras ziņas nosūtīšanas ieraksta nosūtīšanas datumu un ziņas tekstu.

### txt_to_json.py un zinas.txt
Skripts un "avots", kas zinas.json failā izveido jaunu sarakstu ar ziņām - visām ziņām statuss "used" būs 0.

### append_to_json.py un new_zinas.txt
Skripts un "avots", no kura pievieno jaunas rindas zinas.json failā, neizmainot statusu jau esošajām ziņām.

### cik_palika.py
Izprintē, cik neizmantotas ziņas vēl ir palikušas.

## Konfidenciāli dati
(šobrīd nestrādā) Saņēmēja e-pastam ir jāglabājas failā "laimigais.txt".  
App password no sūtītāja e-pasta ir jāglabā failā "parole.txt".

## Bildes
Ziņām var pievienot bildes un PDF failus. Bet tad bildes ir jāglabā mapē "images" un
ziņas tekstam jāpievieno beigās ":/images/pareizs_nosaukums.jpg". Un attiecīgi PDF
failus glabā mapē "attach" un ziņas tekstam pievieno ":/attach/pareizs_nosaukums.pdf".

## Setup
Šobrīd šie faili atrodas uz android telefona, kurā ir ielādēts Termux. 
Automātiskā, regulārā skripta palaišana tiek nodrošināta ar crontab/cronjob. 
E-pasts tiek sūtīts katru nedēļu pirmdien plkst. 7:00.

## Papildus info
Sūtītāja adrese ir vards.uzvards.69420@gmail.com - dummy epasts, 
kuram ir izveidota app password, kas glabājas "parole.txt" failā uz telefona.

## TODO
- Varbūt salabot to lietu, ka encoding salūst, ja lasa saņēmēja epastu no faila (notiek tikai uz telefona(python3.11), no datora(python3.10) nekādu problēmu) 
