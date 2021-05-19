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
import sys

# 1. Create a socket
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()
    
# 2. Bind the socket to an IP address and port
try: 
    mysock.bind(("", 1234)) # First argument is the host. And empty string allows any host to request the server
except socket.error:
    print("Failed to bind")
    sys.exit()
    
# 3. Listen for connection
mysock.listen(5) # Argument is the number of requests allowed to wait for service

# 4. Accept the connection
while True:
    conn, addr = mysock.accept() # Connection and address
    
    # 5. Receive the request
    data = conn.recv(1000)

    if not data:
        break

    # 6. Send a responce
    conn.sendall(data)

conn.close()
mysock.close()
