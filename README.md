# Multiple-Client-Server-Program-in-Python

This TCP Server-Client Communication program consists of two scripts and one config YAML file. 

Purpose of Server.py:
1) Process and respond to Client
2) Broadcast message to all the connected Clients

Purpose of Client.py
1) Send messages entered by the user to the Server
2) Constantly poll for the new messages from Server

Development environment :
Ubuntu 18.04.1 LTS 
Python 3
Editor used : gedit 

 Test Run procedure?
1) Run the Server Script First: python3 TcpServer.py 
2) Once the Server is up, Run the Client Script: python3 TcpClient.py
3) Enter the username to start communicating. 
4) Run Multiple Clients for interactive communication.
