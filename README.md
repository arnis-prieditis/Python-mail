# Python-mail
Python skripts, kas jauzliek uz kkada servera, ka strādā 24/7, lai reizi nedēļā Andrim uz e-pastu atnāktu kāda jauka ziņa. Var arī citā veidā automatizēt sūtīšanu, tā ir vienīgā problēma šobrīd.

insults.json glabā json sarakstu ar objektiem, kas katrs reprezentē ziņas saturu(plain teksta formāts) un tās statusu(vai tā ir jau bijusi nosūtīta). Varbūt vēl varētu pievienot funcionalitāti, ka pielikumus var pievienot.

send_mail.py satur galveno skriptu, kas izmanto insults.json, lai nosūtītu Andrim(šobrī testēšanas nolūkos man pašam) 1 epasta ziņu.
Sūtītāja adrese ir vards.uzvards.69420@gmail.com - dummy epasts, kuram ir izveidota app password, kas ir cieti iekodēta(?) skriptā. Varbūt drošības pēc to vajadzētu glabāt atsevišķā failā, idk.
