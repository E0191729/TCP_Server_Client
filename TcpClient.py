from socket import *
from threading import Thread
from pathlib import Path
import yaml
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
config_file = PATH+'/config.yaml'
my_file     = Path(config_file)
if my_file.is_file():
	with open(config_file) as fp:
	    config = yaml.load(fp)
else:
	print('config.yaml file does not exists. Please make from config.yaml file')
	sys.exit()

clients = {}
addresses = {}

HOST = config['HOST']
PORT = config['PORT']
BUFSIZE = config['BUFFER']

ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def recv():
    while True:
    	try:
    		msg = client_socket.recv(BUFSIZE).decode("utf8")
    		print(msg)
    	except OSError:  # Possibly client has left the chat.
    		sys.exit()
    		break

Thread(target=recv).start()
while True:
    msg = input()
    if msg == "-exit":
    	client_socket.close()
    	print("Bye:) Have a nice Day!")
    if not msg: break
    client_socket.send(bytes(msg, "utf8"))

client_socket.close()
