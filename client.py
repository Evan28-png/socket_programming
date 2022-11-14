from socket import *
import pickle
import time
import sys
client = socket(AF_INET, SOCK_STREAM, proto=0)
client.connect(('127.0.0.1', int(sys.argv[1])))

def send_msg():
    msg = input('Enter message: ')
    msg = msg.encode('utf-8')
    client.send(msg)


while True:
    data = client.recv(1024)
    if data:
        data = pickle.loads(data)
        print(data)
        send_msg()



