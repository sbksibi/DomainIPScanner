# NetDomainResolver

NetDomainResolver is a Python tool that takes an IP address as input and returns the domain name, the domain IP address, and the Domain Controller (AD) IP address. It's useful for network and domain reconnaissance tasks.

## Features

- Reverse DNS lookup to find the domain name associated with an IP address.
- Resolves the domain's IP address.
- Queries the DNS SRV records to find the Domain Controller (AD) IP address.

## Prerequisites

Before running the tool, ensure that you have the following installed:

1. **Python 3.x**: If you don’t have Python installed, download it from [here](https://www.python.org/downloads/).
2. **`dnspython` library**: This tool uses the `dnspython` library for DNS lookups.

### Install Required Libraries

You need to install the `dnspython` package before running the script. To install it, run the following command:

```bash
pip3 install dnspython
```

#### RUN

    python3 DomainIPScanner.py 192.168.1.10

##### EXAMPLE OUTPUT 

    Resolving information for IP: 192.168.1.10

    Domain Name for IP 192.168.1.10: example.com
    Domain IP Address: 93.184.216.34
    Domain Controller Host: dc01.example.com
    Domain Controller IP Address: 192.168.1.5


