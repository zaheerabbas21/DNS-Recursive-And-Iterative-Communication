import socket


LOCALHOST = 'localhost'
PORT = 9000
BUFFER_SIZE = 1024

def clientConnect(message):
    udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientMessage = message
    udpClientSocket.sendto(clientMessage.encode(),(LOCALHOST,PORT))
    serverMessage, serverAddress = udpClientSocket.recvfrom(BUFFER_SIZE)
    serverMessage = serverMessage.decode()
    print(f"Message from server: {serverMessage}")
    print(f"Address of the server: {serverAddress}")
    udpClientSocket.close()