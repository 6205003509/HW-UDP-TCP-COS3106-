from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("Waiting for client...")

while True:
    message,clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8')
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    print('Client:',modifiedMessage)