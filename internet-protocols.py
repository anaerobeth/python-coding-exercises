from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)


import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('foo@example.com', 'bar@example.com',
        """To: foo@example.com
        From: bar@example.com

        Hello!
        """
        )
server.quit()
