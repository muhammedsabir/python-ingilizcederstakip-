import smtplib

sender = 'muhammedsabir14@gmail.com'
receivers = ['muhammed_sabir14@yahoo.com']

message = """From: From Person sample test email msabir
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login("muhammedsabir14@gmail.com","******")
   server.sendmail(sender, receivers, message)
   server.quit()
   print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")
