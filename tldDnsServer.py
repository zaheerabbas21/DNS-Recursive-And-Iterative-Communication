import socket
import dns
import dns.resolver
import dns.query
import dns.message
import dns.message
from helpers import LOCAL_HOST, TLD_SERVER_PORT, BUFFER_SIZE
from helpers import splitInput
from helpers import getInput
from helpers import customPrint


def findOutAuthoritative(userInput, nameServer):
    returnMessage = []
    defaultResolver = dns.resolver.get_default_resolver()
    customPrint("defaultResolver", defaultResolver)
    converToDomainName = dns.name.from_text(userInput)
    customPrint("converToDomainName", converToDomainName)
    numberOfWords = 2
    tldInput = getInput(userInput, numberOfWords)
    customPrint("tldInput", tldInput)
    if len(splitInput(userInput)) > 2:
        message = f"I dont know \"{userInput}\" but I know the address of\
        \"{tldInput}\""
        returnMessage.append(message)
    returnMessage.append(f"Looking up {tldInput} on {nameServer}")
    query = dns.message.make_query(tldInput, dns.rdatatype.NS)
    customPrint("query", query)
    response = dns.query.udp(query, nameServer)
    customPrint("response", response)
    responseCode = response.rcode()
    customPrint("responseCode", responseCode)
    if responseCode != dns.rcode.NOERROR:
        if responseCode == dns.rcode.NXDOMAIN:
            returnMessage.append(f"{tldInput} does not exist.")
            returnMessage.append("Please enter a legible domain")
            return returnMessage
        else:
            returnMessage.append("Please enter a legible domain.")
            return returnMessage
    resourceRecordSet = None
    if len(response.authority) > 0:
        resourceRecordSet = response.authority[0]
        customPrint("response.authority", resourceRecordSet)
    else:
        resourceRecordSet = response.answer[0]
        customPrint("response.answer", resourceRecordSet)
    resourceRecord = resourceRecordSet[0]
    customPrint("resourceRecord", resourceRecord)
    if resourceRecord.rdtype == dns.rdatatype.SOA:
        returnMessage.append(f"Same server is authoritative for {tldInput}")
        customPrint("resourceRecord.rdtype", resourceRecord.rdtype)
    else:
        authoritativeServerName = resourceRecord.target
        customPrint("authoritativeServerName", authoritativeServerName)
        returnMessage.append(
            f"{authoritativeServerName} is authoritative for {tldInput}")
        ipAddressofAuthoritative = defaultResolver.query(
            authoritativeServerName).rrset[0].to_text()
        customPrint("ipAdressofTld", ipAddressofAuthoritative)
        returnMessage.append(
            f"Ip Address of {authoritativeServerName} is {ipAddressofAuthoritative}")
        returnMessage.append(str(authoritativeServerName))
        returnMessage.append(ipAddressofAuthoritative)
        customPrint("returnMessage", returnMessage)
    return returnMessage


def tldDnsServer():
    tldDnsServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        tldDnsServerSocket.bind((LOCAL_HOST, TLD_SERVER_PORT))
        print(
            f"TLD Server is up and running at port:{TLD_SERVER_PORT}")
        while True:
            nameServer, _ = tldDnsServerSocket.recvfrom(BUFFER_SIZE)
            nameServer = nameServer.decode()
            clientMessage, clientAddress = tldDnsServerSocket.recvfrom(
                BUFFER_SIZE)
            userInput = clientMessage.decode()
            print(f"Talking to Client at Address:{clientAddress}")
            print(f"Client Message:{userInput}")
            result = findOutAuthoritative(userInput, nameServer)
            print(result)
            serverMessage = str(result).encode()
            print(serverMessage)
            tldDnsServerSocket.sendto(serverMessage, clientAddress)
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()


tldDnsServer()
