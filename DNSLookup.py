import csv


def _splitQuery(query) -> list:
    splitQuery = query.split('.')
    return splitQuery

def authoritativeDNS(query,authoritativeAddressList):
    finalHostName = query
    for hostName in authoritativeAddressList:
        hostname = hostName.get('hostname')
        ipaddress = hostName.get('ipaddress')
        if finalHostName in hostname:
            print(hostname)
            break
    return ipaddress

def tldDNS(query,tldAddressList)->list:
    splitQuery = _splitQuery(query)
    *args,subdomain,ext = splitQuery
    authoritativeQuery = '.'.join((subdomain,ext))
    print(authoritativeQuery)
    authoritativeList = []
    for address in tldAddressList:
        hostname = address.get('hostname')
        ipaddress = address.get('ipaddress')
        if(hostname.endswith(hostname)):
            authoritativeList.append(address)
    return authoritativeList

def rootDNS(query) -> list:
    splitQuery = _splitQuery(query)
    *args,tldQuery = splitQuery
    print(tldQuery)
    tldList = []
    with open('map.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hostname = row['hostname']
            ipaddress = row['ipaddress']
            if hostname.endswith(tldQuery):
                tldList.append(row)
    return tldList

def localDNS(query):
    tldAddressList = rootDNS(query)
    print(tldAddressList)
    authoritativeAddressList = tldDNS(query,tldAddressList)
    print(authoritativeAddressList)
    finalIpAdress = authoritativeDNS(query,authoritativeAddressList)
    print(finalIpAdress)


print("Enter a Domain Name")
userInput = input()
userInput = userInput.strip().lower()
localDNS(userInput)

