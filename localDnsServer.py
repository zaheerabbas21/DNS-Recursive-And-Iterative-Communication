import socket
import dns
import dns.resolver
from helpers import LOCAL_HOST, LOCAL_DNS_SERVER_PORT, BUFFER_SIZE
from helpers import splitInput
from helpers import ROOT_SERVER_PORT
from helpers import actAsTemporaryClient
from helpers import displayMessages
from helpers import getInputForNextServer


def handleRootServer(userInput, rootNameServer):
    rootResult = actAsTemporaryClient(
        userInput, ROOT_SERVER_PORT, rootNameServer)
    print("Root Result:")
    displayMessages(rootResult)
    ipAddressOfTld = getInputForNextServer(rootResult)
    print(ipAddressOfTld)
    return ipAddressOfTld


def localDnsServer():
    localDnsServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        localDnsServerSocket.bind((LOCAL_HOST, LOCAL_DNS_SERVER_PORT))
        print(
            f"localDNS is up and running and I am listening at Port:{LOCAL_DNS_SERVER_PORT}")
        while True:
            clientMessage, clientAddress = localDnsServerSocket.recvfrom(
                BUFFER_SIZE)
            userInput = clientMessage.decode()
            print(f"Talking to the Client at the Address:{clientAddress}")
            print(f"Client Message:{userInput}")
            message = f"Hang in there client, I will get the IP Address of the requested {userInput} domain"
            message = message.encode()
            localDnsServerSocket.sendto(message, clientAddress)
            defaultResolver = dns.resolver.get_default_resolver()
            rootNameServer = defaultResolver.nameservers[0]
            tldNameServer = handleRootServer(userInput, rootNameServer)
            serverMessage = "".encode()
            localDnsServerSocket.sendto(serverMessage, clientAddress)
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()


localDnsServer()
