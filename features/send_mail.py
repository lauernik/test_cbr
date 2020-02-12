import smtplib
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from os import listdir

# Для запуска локального SMTP сервера:
# python3 -m smtpd -n -c DebuggingServer localhost:1025


def send_email(receiver):
    time_now = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
    sender = "from@test.com"

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = f'website.feature test {time_now}'

    pngfiles = paths_to_png()
    for file in pngfiles:
        with open(file, 'rb') as fp:
            img = MIMEImage(fp.read())
        message.attach(img)

    with smtplib.SMTP("localhost", 1025) as server:
        server.sendmail(sender, receiver, message.as_string())


def paths_to_png():
    pngfiles = ['screenshots/'+file for file in listdir('screenshots/.')]
    return pngfiles
