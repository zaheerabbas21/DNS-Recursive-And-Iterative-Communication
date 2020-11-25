import socket

LOCALHOST = "localhost"
PORT = 9000
SHUT_WR = "SHUT_WR"
BUFFER_SIZE = 1024


def serverConnect(message):
    udpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverMessage = message
    try:
        udpServerSocket.bind((LOCALHOST, PORT))
        print(f"UDP server is ready to receive the messages")

        while True:
            clientMessage, clientAddress = udpServerSocket.recvfrom(
                BUFFER_SIZE)
            clientMessage = clientMessage.decode()
            print(f"Client Address:{clientAddress}")
            print(f"Client Message:{clientMessage}")
            udpServerSocket.sendto(serverMessage.encode(), clientAddress)
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()


if __name__ == '__main__':
    message = "Hello UDP Client, I am a UDP Server"
    serverConnect(message)
