"""
Socket Programming
"""
import socket

s = socket.socket()
print("Socket Created")
"""
There are 65535 Ports in Total.
Ports 1 - 1023 are not usable since they are reserved for the most commonly
used applications.
"""
port = 40874


"""
We will now bind an IP address and a port to the socket
"""
s.bind(("", port))  # This allow us to receive incoming traffic from any IP
print(f"Socket Bound to port '{port}'")

"""
Now we listen to any incoming traffic
"""
s.listen()
print("Socket listening...")

while True:
    connection, address = s.accept()
    print("Got connection from", address)

    # Content sent has to be encoded in binary format
    connection.send(b"Thank you for connecting")

    # This closes the session for the specific client
    connection.close()
