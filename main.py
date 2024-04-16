import socket
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    # Email account details
    gmail_user = 'demo.mail.4044@gmail.com'  # Replace with your email
    gmail_password = 'kaew hixh zvfe uwxv'  # Replace with your password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.close()
        print('Email sent successfully!')
    except Exception as e:
        print('Something went wrong...', e)

def handle_client(client_socket):
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    
    # Notify via email
    subject = "New Client Connected"
    message = "A new client has connected to the server."
    to_email = "pateltirth.tech@gmail.com"  # Replace with recipient's email
    send_email(subject, message, to_email)
    
    client_socket.close()

def start_server():
    # Server configuration
    host = "0.0.0.0"
    port = 9999

    # Create socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket
    server.bind((host, port))

    # Start listening
    server.listen(5)
    print("[*] Listening on %s:%d" % (host, port))

    while True:
        # Accept connections from outside
        client_sock, addr = server.accept()

        # Spin up a thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
