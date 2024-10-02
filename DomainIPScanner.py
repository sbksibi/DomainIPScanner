import sys
import socket
import dns.resolver

def get_domain_name_from_ip(ip_address):
    try:
        # Perform reverse DNS lookup to get the domain name from the IP
        domain_name = socket.gethostbyaddr(ip_address)[0]
        print(f"Domain Name for IP {ip_address}: {domain_name}")
        return domain_name
    except socket.herror:
        print(f"Unable to resolve domain name for IP: {ip_address}")
        return None

def get_dc_ip(domain_name):
    try:
        # Querying the DNS for Domain Controllers
        query = f'_ldap._tcp.dc._msdcs.{domain_name}'
        answers = dns.resolver.resolve(query, 'SRV')
        for rdata in answers:
            # Extracting the target domain controller
            dc_host = str(rdata.target).rstrip('.')
            # Get the IP of the domain controller
            dc_ip = socket.gethostbyname(dc_host)
            print(f"Domain Controller Host: {dc_host}")
            print(f"Domain Controller IP Address: {dc_ip}")
            break  # Print the first Domain Controller found
    except Exception as e:
        print(f"Unable to resolve Domain Controller IP: {e}")

def get_domain_ip(domain_name):
    try:
        # Get the IP address of the domain itself
        domain_ip = socket.gethostbyname(domain_name)
        print(f"Domain IP Address: {domain_ip}")
    except socket.gaierror:
        print(f"Unable to resolve domain IP for {domain_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 filename.py <IP_address>")
        sys.exit(1)

    ip_address = sys.argv[1]
    
    print(f"Resolving information for IP: {ip_address}\n")
    
    # Step 1: Get the domain name from the given IP address
    domain_name = get_domain_name_from_ip(ip_address)
    
    if domain_name:
        # Step 2: Get the Domain IP
        get_domain_ip(domain_name)
        
        # Step 3: Get the Domain Controller (AD) IP
        get_dc_ip(domain_name)
