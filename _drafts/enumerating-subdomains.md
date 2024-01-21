---
layout: post
title: "Infosec: Enumerating subdomains"
tags: infosec, tryhackme
---

Check registered domains via CA

[Google Transparency Report tool](https://transparencyreport.google.com/https/certificates): Use this to find domains and list certificates.

### Use google search

This will exclude all results with "www.domain.com", and include everything else.

```text
-site:www.domain.com site:*.domain.com
```

### Use [ffuf](https://github.com/ffuf/ffuf)

Fast web fuzzer written in Go.

- Via direct subdomain  

```shell
ffuf -w ./SecLists/Discovery/DNS/namelist.txt -u http://FUZZ.domain.com
```

- Via Host header in the request  

```shell
# This enumerates via 'Host' header in the request.
# Run first without -fs, then with by replacing {size} with the common size value from the previous command.
ffuf -w ./SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.domain.com" -u http://www.domain.com -fs {size} 
```

### Other enumeration tools

- [DNSRecon](https://github.com/darkoperator/dnsrecon)

```
pip3 install dnsrecon

dnsrecon -d domain.com
```

- [sublist3r](https://github.com/aboul3la/Sublist3r)

```shell
pip3 install sublist3r

sublist3r -d domain.com
```
