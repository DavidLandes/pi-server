import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "[DISCONNETED] client disconnected."

SERVER = "192.168.1.21" #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    # Add padding to fill header size
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

send("Hello world.")
send("Hello everyone.")
send("Hello tim.")

send(DISCONNECT_MESSAGE)
