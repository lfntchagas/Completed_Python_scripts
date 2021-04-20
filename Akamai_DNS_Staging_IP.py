import dns
from dns import resolver
import argparse


parser = argparse.ArgumentParser(description='return staging IP of a hostname')
parser.add_argument('-d', '--domain',help='Write down the domain name', required=True)
args = parser.parse_args()


def resolve_cname(host):
    '''Resolve cname of the argument host'''

    resolver = dns.resolver.resolve(qname=host, rdtype='CNAME')
    for i in resolver:
        cname_string = str(i)

    list_splited = cname_string.split('.') # split the string in dots
    index = list_splited.index('edgekey') # return index position of edgekey
    list_splited[index] = list_splited[index] + '-staging'
    separator = '.'
    return separator.join(list_splited)


def resolve_a(host):
    '''Resolve the dns type A from the argumennt host'''

    resolver = dns.resolver.resolve(qname=host, rdtype='A')
    for i in resolver:
        result = i
    return result


prompt = '''
- How to test staging environment:

To spoof, enter the domain and IP in your host file, or use testing tools like curl or wfetch.
Host file entry example: {} {}
Note: 
- Don’t execute the tests from either the office or VPN as the most of the office’s IPs are whitelisted in Akamai.
- To make sure you are hitting the staging environment you have to be able to see in the response header the HTTP header: x-akamai-staging: ESSL
- If for some reason you are not able to change your host file, it might means you are getting blocked by xyz, in this case, please inform to me your e-mail so you can be whitelisted.
'''.format(resolve_a(resolve_cname(args.domain)), args.domain)


def main():
    #print(resolve_a(resolve_cname(args.domain)))
    print(prompt)

if __name__ == "__main__":
    main()







