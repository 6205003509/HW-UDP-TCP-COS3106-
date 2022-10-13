from socket import *
from sqlite3 import connect

clientName = 'AbSoLuTeZR0'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((clientName,serverPort))

print("Connected")
sentence = input("Client: ")
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
clientSocket.close()