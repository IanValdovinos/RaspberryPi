# This program sets the Raspberry Pi as a socket server that reacts to
# requests from a IP address lookup on a web browser

import socket
import sys

# Create a socket
try:
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfuly!")
except socket.error:
    print("Failed to create socket.")
    sys.exit()

# Bind the socket to an IP address and port
try:
    ms.bind(("", 80)) # It has to connect to port 80 in order to work via the Web 
    print("Bind successful!")
except socket.error:
    print("Failed to bind.")
    sys.exit()


# Listen for connection
ms.listen(5)

# Accept the connection
conn, addr = ms.accept()

# Confirm request
if conn and addr:
    print("Got a request!")

conn.close()
ms.close()
