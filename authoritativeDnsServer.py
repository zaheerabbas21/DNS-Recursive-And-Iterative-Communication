import socket
import dns
import dns.resolver
import dns.query
import dns.message
import dns.message
from helpers import LOCAL_HOST, AUTHORITATIVE_SERVER_PORT, BUFFER_SIZE
from helpers import splitInput
from helpers import getInput
from helpers import customPrint


def findOutResultantIp(userInput, nameServer):
    returnMessage = []
    defaultResolver = dns.resolver.get_default_resolver()
    customPrint("defaultResolver", defaultResolver)
    converToDomainName = dns.name.from_text(userInput)
    customPrint("converToDomainName", converToDomainName)
    numberOfWords = len(splitInput(userInput))
    authoritativeInput = getInput(userInput, numberOfWords)
    customPrint("authoritativeInput", authoritativeInput)
    returnMessage.append(f"Looking up {authoritativeInput} on {nameServer}")
    query = dns.message.make_query(authoritativeInput, dns.rdatatype.A)
    customPrint("query", query)
    response = dns.query.udp(query, nameServer)
    customPrint("response", response)
    responseCode = response.rcode()
    customPrint("responseCode", responseCode)
    if responseCode != dns.rcode.NOERROR:
        if responseCode == dns.rcode.NXDOMAIN:
            returnMessage.append(f"{authoritativeInput} does not exist.")
            returnMessage.append("Please enter a legible domain")
            return returnMessage
        else:
            returnMessage.append("Please enter a legible domain.")
            return returnMessage
    flag = False
    resourceRecordSet = None
    resourceRecord = ""
    if len(response.answer) > 0:
        resourceRecordSet = response.answer[0]
        customPrint("response.answer", resourceRecordSet)
        resourceRecord = resourceRecordSet[0]
        customPrint("resourceRecord", resourceRecord)
        customPrint("resourceRecord.rdtype", resourceRecord.rdtype)
        if resourceRecord.rdtype != dns.rdatatype.A:
            returnMessage.append(
                f"{userInput} requires another Authoritative Server Call, fetching it directly")
            answer = dns.resolver.resolve(userInput, 'A')
            customPrint("answer", answer)
            resourceRecord = answer[0]
            customPrint("resourceRecord", resourceRecord)
    else:
        returnMessage.append(
            f"{userInput} requires another Authoritative Server Call, fetching it directly")
        answer = dns.resolver.resolve(userInput, 'A')
        customPrint("answer", answer)
        resourceRecord = answer[0]
        customPrint("resourceRecord", resourceRecord)
    customPrint("resourceRecord", resourceRecord)
    finalIPAddress = str(resourceRecord)
    returnMessage.append(f"IP address of the {userInput} is {finalIPAddress}")
    returnMessage.append(finalIPAddress)
    return returnMessage


def authoritativeDnsServer():
    authoritativeDnsServerSocket = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)
    try:
        authoritativeDnsServerSocket.bind(
            (LOCAL_HOST, AUTHORITATIVE_SERVER_PORT))
        print(
            f"Authoritative Server is up and running at port:{AUTHORITATIVE_SERVER_PORT}")
        while True:
            nameServer, _ = authoritativeDnsServerSocket.recvfrom(BUFFER_SIZE)
            nameServer = nameServer.decode()
            clientMessage, clientAddress = authoritativeDnsServerSocket.\
                recvfrom(BUFFER_SIZE)
            userInput = clientMessage.decode()
            print(f"Talking to Client at Address:{clientAddress}")
            print(f"Client Message:{userInput}")
            result = findOutResultantIp(userInput, nameServer)
            print(result)
            serverMessage = str(result).encode()
            print(serverMessage)
            authoritativeDnsServerSocket.sendto(serverMessage, clientAddress)
    except KeyboardInterrupt:
        print("\nStopping the server")
        print("........")
        print("........")
        print("You Stopped the server")
        exit()
    except:
        print("Something went wrong")
        exit()


authoritativeDnsServer()
