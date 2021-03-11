import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "[DISCONNETED] client disconnected."

SERVER = "192.168.1.21" #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

SESSION_LIVE = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def try_cmd(cmd):
    if type(cmd) == str:
        if cmd == "quit" or cmd == "q":
            print(f"[DISCONNECT] {SERVER} session has ended.")
            send(DISCONNECT_MESSAGE)
            return False

        elif cmd[0:4] == "send" and cmd[4:5] == " ":
            data = cmd[5:]
            send(data)
            return f""


    print(f"Invalid command [{cmd}].")
    return True

def handle_input():
    args = input(">>> ")
    res = try_cmd(args)
    return res

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    # Add padding to fill header size
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)


# Begin main loop.
while SESSION_LIVE:
    res = handle_input()
    if type(res) == bool:
        SESSION_LIVE = res
    else:
        print(f"{res}")

