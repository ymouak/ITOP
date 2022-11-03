import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from requests.auth import HTTPBasicAuth
from datetime import date
msg = MIMEMultipart()
Serveur_SMTP = 'xxxxxxxx'
Port_SMTP = 25
Email_login = str( sys.argv[1] )
Email_mdp  = str( sys.argv[2] )
now = date.today()
sender = 'itopincident@attijariwafa.com'
recipients = 'a.bousbaa@attijariwafa.com,h.elaamraoui@attijariwafa.com,a.houry@attijariwafa.com,k.aziz@attijariwafa.com,y.mouak@attijariwafa.com'
msg['From'] =  sender
msg['To'] = recipients
msg['Subject'] ='Rapport des Changements monetique passes en production'

r = requests.get('https://itop.attijariwafa.net/webservices/export-v2.php?format=spreadsheet&login_mode=basic&date_format=Y-m-d+H%3Ai%3As&query=11', auth=HTTPBasicAuth(str( sys.argv[3] ), str( sys.argv[4] )), verify=False)
message = r.text.encode('utf-8')
msg.attach(MIMEText(message,'html'))
mailserver = smtplib.SMTP(Serveur_SMTP , Port_SMTP)
mailserver.ehlo()
mailserver.login(Email_login,Email_mdp)
mailserver.sendmail( sender, recipients.split(','), msg.as_string())
mailserver.quit()

print ('Notification ok',now.strftime("%d/%m/%Y %H:%M:%S"))

