"""
This program creates a generic network client 

1. Create a socket
2. Connect socket to server
3. Send some data (a request)
4. Receive some data (a response)
5. Close the socket
"""

import socket

# 1. Create a socket
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET declares Address Family Internet
# SOCK_STREAM indicates TCP

# 2. Connect socket to server
host = socket.gethostbyname("www.google.com") # Gets IP address by a domain name 

mysock.connect((host, 80)) # Connect client to host. 80 refers to port 8 for web traffic

# 3. Send some data
message = "GET / HTTP/1.1\r\n\r\n" # HTTP GET request

mysock.sendall(message)

# 4. Receive some data
data = mysock.recv(1000) # Argument is the maximum number of bytes expected

# 5. Closing a socket
mysock.close()
