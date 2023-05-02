# NOTE: This is the client side script
import socket


s = socket.socket()
print("Socket Created")

# Here, we define the IP Address and Port we want to connect to
s.connect(("127.0.0.1", 40874))

"""
This allows the client to only receive 1024 bytes of data
If the server is sending packets that are larger than 1024 bytes, it has to
fragment the packets to 1024 bytes each so that they can be received by the
client
"""
print((s.recv(1024)))

s.close()
