import RPi.GPIO as GPIO
import time
import socket

# Setup LED GPIO and LED
GPIO.setmode(GPIO.BOARD)

led_pin = 10
GPIO.setup(led_pin, GPIO.OUT)

# Create a socket
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket
ms.bind(("", 1234))

# Listen for connection
print("Waiting for connection...")
ms.listen(5)



while True:
    # Accept the connection
    conn, addr = ms.accept() # Connection and address
    print("Connected!")
    
    # Receive the request
    data = conn.recv(1000)
    print("Request received:", data)

    # Perform operation based on client request
    if data == b"quit":
        print("Closing server...")
        break
    elif data == b"on":
        GPIO.output(led_pin, True)
        print("LED turned on")
    elif data == b"off":
        GPIO.output(led_pin, False)
        print("LED turned off")
    else:
        print("No valid command received.")


# Close all connections when done
conn.close()
ms.close()




