import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
from os import listdir

# Для запуска локального SMTP сервера:
# python3 -m smtpd -n -c DebuggingServer localhost:1025
# Проверка отображения производилась на сервисе mailtrap.io


def send_email(receiver):
    time_now = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
    sender = "from@test.com"

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = f'website.feature test {time_now}'

    img_tags = ''
    pngfiles = paths_to_png()
    if pngfiles:
        for file in pngfiles:
            with open(file, 'rb') as fp:
                img = base64.b64encode(fp.read()).decode()
                img_tags += f'<img src="data:image/jpg;base64,{img}">'
    else:
        img_tags = '<p>Во время теста что-то пошло не так.</p>'

    html = f"<html><body>{img_tags}</body></html>"

    message.attach(MIMEText(html, 'html'))

    with smtplib.SMTP("localhost", 1025) as server:
        server.sendmail(sender, receiver, message.as_string())


def paths_to_png():
    pngfiles = ['screenshots/'+file for file in listdir('screenshots/.')]
    return pngfiles
