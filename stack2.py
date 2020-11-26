
import sys
import dns
import dns.resolver


def customPrint(name, value):
    print(name)
    print(value)
    print(type(value))
    print("$#####$")
    print()


def query_authoritative_ns(domain, log=lambda msg: None):

    default = dns.resolver.get_default_resolver()
    customPrint("default", default)
    ns = default.nameservers[0]
    customPrint("ns", ns)
    n = domain.split('.')
    customPrint("n", n)
    for i in range(len(n), 0, -1):
        sub = '.'.join(n[i-1:])
        customPrint("sub", sub)
        log('Looking up %s on %s' % (sub, ns))
        query = dns.message.make_query(sub, dns.rdatatype.NS)
        customPrint("query", query)
        response = dns.query.udp(query, ns)
        customPrint("response", response)
        rcode = response.rcode()
        customPrint("rcode", rcode)
        if rcode != dns.rcode.NOERROR:
            if rcode == dns.rcode.NXDOMAIN:
                raise Exception('%s does not exist.' % (sub))
            else:
                raise Exception('Error %s' % (dns.rcode.to_text(rcode)))

        if len(response.authority) > 0:
            rrsets = response.authority
            customPrint("rrsets", rrsets)
        elif len(response.additional) > 0:
            rrsets = [response.additional]
            customPrint("rrsets", rrsets)
        else:
            rrsets = response.answer
            customPrint("rrsets", rrsets)
        # Handle all RRsets, not just the first one
        for rrset in rrsets:
            customPrint("rrset", rrset)
            for rr in rrset:
                customPrint("rr", rr)
                if rr.rdtype == dns.rdatatype.SOA:
                    log('Same server is authoritative for %s' % (sub))
                    customPrint("rr.rdtype", rr.rdtype)
                elif rr.rdtype == dns.rdatatype.A:
                    ns = rr.items[0].address
                    customPrint("rr.rdtype", rr.rdtype)
                    customPrint("ns", ns)
                    log('Glue record for %s: %s' % (rr.name, ns))
                elif rr.rdtype == dns.rdatatype.NS:
                    authority = rr.target
                    customPrint("rr.rdtype", rr.rdtype)
                    customPrint("authority", authority)
                    ns = default.query(authority).rrset[0].to_text()
                    customPrint("ns", ns)
                    log('%s [%s] is authoritative for %s; ttl %i' %
                        (authority, ns, sub, rrset.ttl))
                    result = rrset
                    customPrint("result", result)
                else:
                    # IPv6 glue records etc
                    #log('Ignoring %s' % (rr))
                    pass
    customPrint("result", result)
    return result


def log(msg):
    sys.stderr.write(msg + u'\n')


for s in sys.argv[1:]:
    print(query_authoritative_ns(s, log))
