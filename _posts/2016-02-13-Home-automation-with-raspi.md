---
layout: post
title: Home automation with Raspberry Pi
description: This is the first post!
published: true
categories: [raspberry pi]
tags: [raspi, ssh, howto]
comments: true
---

I ordered a Raspberry Pi model B a lot of time ago, and I always used it as home server/media center. What about trying something new?

If you don't know where to start, take a look here: []

Alarm
-----
Requirements:  
Raspberry Pi attached with Ethernet cable or WiFi, Motion sensor.

Light sensor
------------
Requirements:  
Raspberry Pi attached with Ethernet cable or WiFi, Motion Sensor, Relay.


#### Setup
Let's set up the machine: (Raspbian Jessie)  
{{site.url}}
After the basic installation of the system, we should change immediately the base login informations, now as  `pi:raspberry`.

Edit the password for `pi` account
```bash
$ sudo passwd pi
Insert new UNIX password:
```

Install dependencies

sudo apt-get install

#### Workers

```
sudo apt-get install rabbitmq-server
```
