#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from pathlib import Path
import yaml
import os

PATH = os.path.dirname(os.path.abspath(__file__))
config_file = PATH+'/config.yaml'
my_file     = Path(config_file)
if my_file.is_file():
	with open(config_file) as fp:
	    config = yaml.load(fp)
else:
	pprint('config.yaml file does not exists. Please make from config.yaml file')
	sys.exit()

clients = {}
addresses = {}

HOST = config['HOST']
PORT = config['PORT']
BUFSIZE = config['BUFFER']

ADDR = (HOST, PORT)

Server_socket = socket(AF_INET, SOCK_STREAM)
Server_socket.bind(ADDR)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = Server_socket.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome!Please enter your name:", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZE).decode("utf8")
    welcome = 'Welcome %s!.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    if msg != bytes("-exit", "utf8"):
    		broadcast(bytes(msg, "utf8"))
    clients[client] = name

while True:
    msg = client.recv(BUFSIZE)
    if msg != bytes("-exit", "utf8"):
        broadcast(msg, name+": ")
    else:
        client.send(bytes("-exit", "utf8"))
        client.close()
        del clients[client]
        broadcast(bytes("%s has left the chat." % name, "utf8"))
        break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


if __name__ == "__main__":
    Server_socket.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    Server_socket.close()

