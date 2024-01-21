---
layout: post
title: Nginx, uwsgi, supervisor with multiple Django installations on HTTP/2
description: "Serve multiple django apps via uWSGI and NGINX on HTTP/2"
categories: [webdev, sys, devops]
tags: [nginx, webdev, uWSGI, django, devops]
---

# Django

Our main file in django is wsgi.py: 
```python


```


# NGINX

NGINX is a high-performance web server. 
In this configuration is used as reverse proxy, to redirect the requests to the right 
responder and serve static files directly. 
Current browsers support HTTP/2 only over SSL, so we need a valid certificate.
I will probably write a See also [Request a certificate with letsencrypt]().

```
server {
    listen 443 http2 ssl;

    server_name localhost;

    # Certificates path
    # The intermediate certificate should be appended to the central 
    .key
    .pem

    # Include all alias locations for installed django apps
    include /etc/nginx/sites-available/locations/app*.conf;
}
```

Tree view from `/etc/nginx`.
```
.
|-- conf.d
|-- fastcgi_params
|-- koi-utf
|-- koi-win
|-- mime.types
|-- naxsi_core.rules
|-- naxsi.rules
|-- naxsi-ui.conf.1.4.1
|-- nginx.conf
|-- proxy_params
|-- scgi_params
|-- sites-available
|   `-- apps
|       |-- locations
|       |   |-- nx_dev9_1.conf
|       |   `-- nx_dev_9.conf
|       `-- nginx.conf
|-- sites-enabled
|   `-- nginx.conf -> /etc/nginx/sites-available/apps/nginx.conf
|-- uwsgi_params
`-- win-utf
```


# Supervisor

Supervisor will manage the uwsgi-emperor instance, to

```INI
[program:uwsgi-emperor]
user = uwsgi
group = uwsgi
command = /home/matcom/start_emperor.sh
autostart = true
autorestart = true
stopsignal = INT
environment = LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
```


# uWSGI Emperor

![Emperor and vassals](http://retajm9g1.weebly.com/uploads/1/0/1/1/10118395/5356331_orig.gif?0)

The emperor mode allows uWSGI to run without directly spawn a target instance.
Will watch for available vassals with one of the specified **imperial monitors**, managing their lifespan.  
Adding a vassal configuration will spawn, editing will reload, deleting will kill.


## Vassals config example

**vassal_1.ini**

```INI
[uwsgi]
; socket file
socket = /tmp/app1.sock
; mount apps
mount = /app1=/home/matcom/proj_1/wsgi.py
; rewrite SCRIPT_NAME and PATH_INFO accordingly
manage-script-name = true
```

**vassal_2.ini**

```INI
[uwsgi]
; socket file
socket = /tmp/app2.sock
; mount apps
mount = /app2=/home/matcom/proj_2/wsgi.py
; rewrite SCRIPT_NAME and PATH_INFO accordingly
manage-script-name = true
```
