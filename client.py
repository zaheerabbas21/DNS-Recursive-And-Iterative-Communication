# # import csv

# # with open('eduTDL.csv') as f:
# #     reader = csv.reader(f,delimiter=',')
# #     next(reader)
# #     for row in reader:
# #         hostname = row[0]
# #         ipaddress = row[1]
# #         if hostname.endswith('com'):
# #             print(hostname)


# # with open('eduTDL.csv','r') as c:
# #     reader = csv.DictReader(c)
# #     # print("HOSTS  ------> IPADDRES")
# #     for row in reader:
# #         hostname = row['hostname']
# #         ipaddress = row['ipaddress']
# #         # print(hostname)
# #         if hostname.endswith('edu'):
# #             print(hostname)

# # print('Enter the domain name')
# # userInput = input()
# # userInput = userInput.split('.')
# # userInput = userInput[::-1]
# # print(userInput)

# # import socket
# # ipaddress = "74.84.128.9"
# # print(socket.gethostbyaddr(ipaddress))

# import os
# import csv
# import subprocess

# hostnameList = ['github.com','gitlab.com','google.com','facebook.com','stackoverflow.com','amazon.com','jnnce.ac.in','youtube.com']

# for name in hostnameList:
#     command = f'dig +short @8.8.8.8 {name} NS'
#     output = subprocess.check_output(command,shell=True)
#     print(name)
#     print(output.decode(),end='')
#     # os.system(command)name
#     # with open('file.txt', 'r') as f:
#     #     with open('map.csv','a',newline='') as mapFile:
#     #         headers = ['hostname','ipaddress']
#     #         writer = csv.DictWriter(
#     #             mapFile, fieldnames=headers,delimiter=",",quoting=csv.QUOTE_NONE,quotechar=' ',escapechar='\t')
#     #         if mapFile.tell() == 0:
#     #             writer.writeheader()
#     #         for row in f:
#     #             writer.writerow({headers[0]:name,headers[1]:row})
#     #             print(row)
#     #             print('-------------------------')
#     # print(type(output))

# # import socket
# # import re
# # pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

# # # mappingDict = dict()
# # ipaddressList = []

# # def getIpAdress(hostnameList):
# #     for hostname in hostnameList:
# #         addressInfoList = socket.getaddrinfo(hostname,port=53)
# #         # print(str(hostname) + '------------------>' + str(addressInfoList))
# #         print(hostname)
# #         for addressInfo in addressInfoList:
# #             # print(addressInfo)
# #             ipv4,*args = addressInfo[4]
# #             matchIpv4 = pat.match(ipv4)
# #             if matchIpv4 and ipv4 not in ipaddressList:
# #                 ipaddressList.append(ipv4)
# #                 print(ipv4)
# #             # print(type(ipv4))
# #         print("----------------------")
# #         print()
# #         # print(type(addressInfo))


from sys import *
from localDnsClient import *
import re

def isValid(userInput):
    regex = r"([a-z]+\.[a-z]+)+"
    result = re.findall(regex,userInput)
    if len(result) > 0:
        return True
    else:
        return False


print("Please Enter the domain name: ")
print("Example : \"domain.com\"")
userInput = input()
result = isValid(userInput)
if result:
    localDnsClient(userInput)
else:
    print("Please enter a domain name in the correct format")
# localDnsClient(userInput)
print("Done")
