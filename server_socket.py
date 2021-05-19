"""
This program creates a generic network server

1. Create a socket
2. Bind the socket to an IP address and port
3. Listen for connection
4. Accept the connection
5. Receive the request
6. Send a responce 
"""

import socket

# 1. Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to an IP address and port 
mysock.bind("", 1234) # First argument is the host. And empty string allows any host to request the server

# 3. Listen for connection
mysock.listen(5) # Argument is the number of requests allowed to wait for service

# Accept the connection, and Receive the request
conn, addr = mysock.accept() # Connection and address 
