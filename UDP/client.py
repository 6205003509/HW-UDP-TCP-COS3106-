from socket import*

serverName = 'AbSoLuTeZR0'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Client: ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()