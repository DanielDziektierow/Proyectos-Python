from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP

mensaje= MIMEMultipart("plain")
mensaje["From"]=""
mensaje["To"]= ""
mensaje["Subject"]= "Correo de prueba"

men=" "

smtp= SMTP("smtp.live.com")
smtp.starttls()
smtp.login