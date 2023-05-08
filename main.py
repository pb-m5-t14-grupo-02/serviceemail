import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "clausManAPIs@hotmail.com"
receiver = "toyeb13549@soombo.com"
password = "chuvaNaB@nh&1ra"

html = """
<html>
  <body>
    <p>Olá, este é um email em HTML!</p>
    <p>Aqui está uma imagem:</p>
    <img src="https://bit.ly/42c7Avl">
  </body>
</html>
"""

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "This is TEST"
msg.attach(MIMEText(html, "html"))

def send_mail():
  with smtplib.SMTP("smtp-mail.outlook.com", 587) as smtp:
      smtp.starttls()
      smtp.login(sender, password)
      smtp.sendmail(sender, receiver, msg.as_string())
send_mail()

