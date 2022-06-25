import email.message
import smtplib

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=attachment_file_name)


def send_email(message):
    """Sends the message to the configured SMTP server"""


mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
mail_server.quit()


def generate_error_report(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message = [FROM] = sender
    message = [TO] = recipient
    message = [Subject] = subject
    message.set_content(body)

    return message
