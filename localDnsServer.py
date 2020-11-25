import socket
from helpers import LOCAL_HOST, LOCAL_DNS_SERVER_PORT, BUFFER_SIZE, FLAG
from helpers import splitInput


def sendDataToClient():
    pass


def localDnsServer(message):
    localDnsServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverMessage = message.encode()
    try:
        localDnsServerSocket.bind((LOCAL_HOST, LOCAL_DNS_SERVER_PORT))
        print(f"localDNS is up and running")
        FLAG = 1
        while True:
            clientMessage, clientAddress = localDnsServerSocket.recvfrom(
                BUFFER_SIZE)
            userInput = clientMessage.decode()
            localDnsServerSocket.sendto(serverMessage, clientAddress)
            print(f"Client Address:{clientAddress}")
            print(f"Client Message:{userInput}")
            splitResult = splitInput(userInput)
            print(f"splitResult {splitResult}")
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()


message = "Some Domain Name"
localDnsServer(message)
