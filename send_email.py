import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "Enter email address"
    password = "Enter API password"

    receiver = "Enter email address"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

send_email("Hello, learning Python now?")
