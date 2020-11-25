import sys
import dns
import dns.name
import dns.query
import dns.resolver

def customPrint(name,value):
    print(name)
    print(value)
    print(type(value))
    print("$#####$")
    print()

def get_authoritative_nameserver(domain, log=lambda msg: None):
    customPrint("domain",domain)
    n = dns.name.from_text(domain)
    customPrint("n",n)
    depth = 2
    default = dns.resolver.get_default_resolver()
    nameserver = default.nameservers[0]
    customPrint("nameserver",nameserver)
    last = False
    while not last:
        s = n.split(depth)
        customPrint("s",s)
        last = s[0].to_unicode() == u'@'
        sub = s[1]
        customPrint("last",last)
        customPrint("sub", sub)
        log('Looking up %s on %s' % (sub, nameserver))
        query = dns.message.make_query(sub, dns.rdatatype.NS)
        customPrint("query", query)
        response = dns.query.udp(query, nameserver)
        customPrint("response",response)
        rcode = response.rcode()
        customPrint("rcode",rcode)
        if rcode != dns.rcode.NOERROR:
            if rcode == dns.rcode.NXDOMAIN:
                raise Exception('%s does not exist.' % sub)
            else:
                raise Exception('Error %s' % dns.rcode.to_text(rcode))

        rrset = None
        customPrint("response.authority",response.authority)
        if len(response.authority) > 0:
            rrset = response.authority[0]
        else:
            rrset = response.answer[0]
        customPrint("rrset",rrset)

        rr = rrset[0]
        customPrint("rr",rr)
        if rr.rdtype == dns.rdatatype.SOA:
            customPrint("rr.rdtyp",rr.rdtype)
            customPrint("dns.rdatatype.SOA",dns.rdatatype.SOA)
            log('Same server is authoritative for %s' % sub)
        else:
            authority = rr.target
            customPrint("rr.target",rr.target)  
            log('%s is authoritative for %s' % (authority, sub))
            nameserver = default.query(authority).rrset[0].to_text()
            customPrint("nameserver2",nameserver)

        depth += 1
        customPrint("depth2",depth)
    customPrint("nameserver",nameserver)
    return nameserver


def log(msg):
    print(msg)


print(get_authoritative_nameserver(sys.argv[1], log))
