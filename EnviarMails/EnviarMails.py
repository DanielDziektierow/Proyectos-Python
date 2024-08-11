import smtplib 
import win32com.client as win32

outlook= win32.Dispatch("Outlook.Application")

mail= outlook.CreateItem(0)

mail.To= 'dz09dz@hotmail.com'

mail.Subject= 'Prueba de mail'

mail.Body= 'Esto es un mensaje de prueba'

mail.Send()