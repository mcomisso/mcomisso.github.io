---
layout: post
title: 'Infosec: Enumerating subdomains'
tags: infosec, tryhackme
date: 2022-03-03 23:27 +0000
---
> This posts lists a few ways to enumerate subdomains.

# Check registered domains via CA

[Google Transparency Report tool](https://transparencyreport.google.com/https/certificates): Use this to find domains and list certificates.

# Use google search

This will exclude all results with "www.domain.com", and include everything else.

```
-site:www.domain.com site:*.domain.com
```

# Brute forcing

## Using [ffuf](https://github.com/ffuf/ffuf)

Fast web fuzzer written in Go.

- ## Via direct subdomain  

```shell
ffuf -w ~/infosec/SecLists/Discovery/DNS/namelist.txt -u http://FUZZ.domain.com
```

- ## Via Host header in the request  

```shell
# This enumerates via 'Host' header in the request
ffuf -w ~/infosec/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.domain.com" -u http://www.domain.com -fs 2395
```

---  

Similar enumeration tools:

- [DNSRecon](https://github.com/darkoperator/dnsrecon)

```
pip3 install dnsrecon
```

- [sublist3r](https://github.com/aboul3la/Sublist3r)

```shell
# Installation
pip3 install sublist3r
```