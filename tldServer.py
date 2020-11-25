import socket
from helpers import LOCAL_HOST, TLD_SERVER_PORT, BUFFER_SIZE, FLAG


def tldServer(message):
    tldServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverMessage = message.decode()
    try:
        tldServerSocket.bind((LOCAL_HOST, TLD_SERVER_PORT))
        print(f"TLD server is doing its job")

        while True:
            clientMessage, clientAddress = tldServerSocket.recvfrom(
                BUFFER_SIZE)
            clientMessage = clientMessage.decode()
            print(f"Client Address:{clientAddress}")
            print(f"Client Message:{clientMessage}")
            tldServerSocket.sendto(serverMessage.encode(), clientAddress)
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()
