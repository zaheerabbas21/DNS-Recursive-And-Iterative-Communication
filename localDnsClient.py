import socket
from helpers import LOCAL_HOST, LOCAL_DNS_SERVER_PORT, BUFFER_SIZE


def localDnsClient(message):
    localDnsClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientMessage = message.encode()
    connectingAddress = (LOCAL_HOST, LOCAL_DNS_SERVER_PORT)
    localDnsClientSocket.sendto(clientMessage, connectingAddress)
    serverMessage, serverAddress = localDnsClientSocket.recvfrom(BUFFER_SIZE)
    serverMessage = serverMessage.decode()
    print(f"Message from server: {serverMessage}")
    print(f"Address of the server: {serverAddress}")
    localDnsClientSocket.close()
