import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import smtplib
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
local_ip_address = s.getsockname()[0]

command = str(local_ip_address)
print("Sendng: %s" % command)
fromaddr = "from address"
toaddr = "to address"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Pi Address'
part = MIMEBase('application', "octet-stream")
#part.set_payload(open(command, "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename=%s' % command)

body = command
msg.attach(MIMEText(body, "plain"))
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("username", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
