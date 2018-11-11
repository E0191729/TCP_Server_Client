from socket import *
from threading import Thread
import sys

HOST = ''
PORT = 33000
BUFSIZE = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def recv():
    while True:
    	try:
    		msg = client_socket.recv(BUFSIZE).decode("utf8")
    		print(msg)
    	except OSError:  # Possibly client has left the chat.
    		break

Thread(target=recv).start()
while True:
    msg = input()
    if msg == "{quit}":
        client_socket.close()
    if not msg: break
    client_socket.send(bytes(msg, "utf8"))

client_socket.close()
