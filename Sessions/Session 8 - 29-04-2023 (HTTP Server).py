import requests
from bs4 import BeautifulSoup
import http.server
import socketserver
import dns.resolver

"""
TCP 3 Way Handshake
Client -> [Syn] -> Server

Server -> [Syn] -> Client
Server -> [Ack] -> Client

Client -> [Ack] -> Server
"""

"""
HTTP Requests
"""
session = requests.Session()
response = session.get("https://www.google.com")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("title")
paragraph = soup.find_all("p")
links = soup.find_all("a")
[print(link) for link in links]


"""
HTTP Server
"""
PORT = 8080
IP = "127.0.0.1"
handler = http.server.SimpleHTTPRequestHandler
http_server = socketserver.TCPServer((IP, PORT), handler)

print(f"Serving at port '{PORT}'...")
http_server.serve_forever()


"""
DNS Resolution
"""
result = dns.resolver.resolve("google.com", "A")
for value in result:
    print("A record: ", value.to_text())
