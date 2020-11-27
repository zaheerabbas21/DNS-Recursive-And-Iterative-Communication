import socket
LOCAL_HOST = "localhost"
LOCAL_DNS_SERVER_PORT = 9000
ROOT_SERVER_PORT = 9001
TLD_SERVER_PORT = 9002
AUTHORITATIVE_SERVER_PORT = 9003
BUFFER_SIZE = 65535


def customPrint(name, value):
    print(name)
    print(value)
    print(type(value))
    print("$#####$")
    print()


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
    cleanList.reverse()
    ipAddressOfTld = cleanList[0]
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


def getInput(givenInput, numberOfWords):
    result = splitInput(givenInput)
    customPrint("result", result)
    result.reverse()
    customPrint("reverseSplitInput", result)
    returningString = ""
    customPrint("returningString", returningString)
    for i in range(numberOfWords):
        returningString = result[i] + "." + returningString
        customPrint("returningString", returningString)
    return returningString


def splitInput(userInput) -> list:
    splitDomainName = userInput.split('.')
    return splitDomainName
