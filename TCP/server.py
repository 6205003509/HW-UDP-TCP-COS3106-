from socket import *
from sqlite3 import connect

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print('Waiting for client...')
while True:
   connectionSocket, addr = serverSocket.accept()
   sentence = connectionSocket.recv(1024).decode('utf-8')
   capitalizedSentence = sentence
   connectionSocket.send(capitalizedSentence.encode("utf-8"))
   print('Client:', capitalizedSentence)
   connectionSocket.close()