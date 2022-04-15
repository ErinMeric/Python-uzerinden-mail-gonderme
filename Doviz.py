import smtplib


content = "bla bla bla bla bla"

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()


mail.starttls()

mail.login("User email address","User password")

mail.sendmail("batugs1453@gmail.com","batugs1453@gmail.com",content)