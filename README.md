# Python-mail
Python skripts, kas jauzliek uz kkada servera, ka strādā 24/7, lai reizi nedēļā Andrim uz e-pastu atnāktu kāda jauka ziņa.

insults.json glabā json sarakstu ar objektiem, kas katrs reprezentē ziņu un tās statusu(vai tā ir jau izmantota/nosūtīta).

send_mail.py satur galveno skriptu, kas izmanto insults.json, lai nosūtītu Andrim(šobrī testēšanas nolūkos man pašam) 1 epasta ziņu.
Sūtītāja adrese ir vards.uzvards.69420@gmail.com - dummy epasts, kuram ir izveidota app password, kas ir cieti iekodēta(?) skriptā.
Varbūt drošības pēc to vajadzētu glabāt atsevišķā failā, idk.

Lai projekts nostrādātu līdz galam, jātiek galā ar vēl 2 problēmām:
  1) Ziņas teksta formatēšana - pagaidām piemērā, kur ir 2 rindas, tiek nosūtīta tikai 2. rinda.
  2) VPS servisa atrašana, kas ļautu vismaz dažus mēnešus par brīvu izmantot virtuālu serveri, uz kura uzlikt un automatizēt šo skriptu.Vai arī pats tādu uztaisi.
