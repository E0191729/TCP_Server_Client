# Multiple-Client-Server-Program-in-Python

This TCP Server-Client Communication program consists of two scripts and one config YAML file. 

Purpose of TcpServer.py:
1) Process and respond to Client
2) Broadcast message to all the connected Clients

Purpose of TcpClient.py
1) Send messages entered by the user to the Server
2) Constantly poll for the new messages from Server

Purpose of config.yaml
1) Easy access for the user to change the port number, Hostname and Buffer Size
2) Any change in the config.yaml file will update both Client and Server Scripts

Development environment :
Ubuntu 18.04.1 LTS 
Python 3
Editor used : gedit 

 Test Run procedure?
1) Run the Server Script First: python3 TcpServer.py 
2) Once the Server is up, Run the Client Script: python3 TcpClient.py
3) Enter the username to start communicating. 
4) Run Multiple Clients for interactive communication.
