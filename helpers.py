import socket
LOCAL_HOST = "localhost"
LOCAL_DNS_SERVER_PORT = 9000
ROOT_SERVER_PORT = 9001
TLD_SERVER_PORT = 9002
AUTHORITATIVE_SERVER_PORT = 9003
BUFFER_SIZE = 2324


def getInputForNextServer(listOfMessages):
    print(listOfMessages)
    print(type(listOfMessages))
    cleanList = []
    for message in listOfMessages:
        message = message.strip()
        message = message.replace("'", "")
        cleanList.append(message)
    print(cleanList)
    ipAddressOfTld = str
    count = 0
    for mes in cleanList:
        if(count == len(cleanList)-1):
            ipAddressOfTld = mes
            print(ipAddressOfTld)
        count += 1
    return ipAddressOfTld


def displayMessages(listOfMessages):
    for message in listOfMessages:
        message = message.replace("'", "")
        print(message)


def actAsTemporaryClient(message, connectingPort, nameServer):
    tempClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    queryMessage = message.encode()
    nameServer = nameServer.encode()
    connectingAddress = (LOCAL_HOST, connectingPort)
    tempClientSocket.sendto(nameServer, connectingAddress)
    tempClientSocket.sendto(queryMessage, connectingAddress)
    serverMessage, serverAddress = tempClientSocket.recvfrom(BUFFER_SIZE)
    serverMessage = serverMessage.decode()
    print(f"Message from server: {serverMessage}")
    print(f"Address of the server: {serverAddress}")
    print(type(serverMessage))
    listOfMessages = serverMessage.strip('[]').split(',')
    print(listOfMessages)
    print(type(listOfMessages))
    tempClientSocket.close()
    return listOfMessages


def getInput(result, wantedWordIndex):
    return result[wantedWordIndex]


def splitInput(userInput) -> list:
    splitDomainName = userInput.split('.')
    return splitDomainName
