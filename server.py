from socket import *
import sys
from threading import *
import pickle
import time
import datetime
from concurrent.futures import *

class Client_sock:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr

    def send_msg(self, msg):
#        msg = msg.encode('utf-8')
        self.sock.send(msg)

    def receive(self):
        msg = self.sock.recv(1024).decode('utf-8')
        return msg

class Server:
    sock = None

    def __init__(self):
        self.hostname = '127.0.0.1'
        self.port = int(sys.argv[1])
        self.address = (self.hostname, self.port)

    def create(self):
        sock = socket(AF_INET, SOCK_STREAM, proto=0)
        sock.bind(self.address)
        return sock

    def listen(self):
        sock = self.create()
        Server.sock = sock
        sock.listen()
        print(f'Server listening on evan-pc:{self.port}')

    def display(self):
        string = {'1': 'date', '2': 'exit'}
        string = pickle.dumps(string)
        return string

    def accept(self):
        client_sock, addr = Server.sock.accept()
        client = Client_sock(client_sock, addr)
        print(f'{client.addr} connected')
        return client

    def handle(self, client):
        display = self.display()
        client.send_msg(display)
        while True:
            while True:
                reply = client.receive()
                if reply:
                    break
            print(reply)
            date = datetime.date.today()
            date = pickle.dumps(date)
            client.send_msg(date)


    

server = Server()
def start():
    server.listen()
    while True: 
        client = server.accept()
        if not client:
            continue
        thread = Thread(target=server.handle, args=[client])
        thread.start()
        continue


start()
