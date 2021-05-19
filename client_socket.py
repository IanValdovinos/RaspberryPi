"""
This program creates a generic network client 

1. Create a socket
2. Connect socket to server
3. Send some data (a request)
4. Receive some data (a response)
5. Close the socket
"""

import socket

mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
