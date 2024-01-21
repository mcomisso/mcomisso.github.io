---
layout: post
title: "#14 - home automation"
description: "Home automation and domotics"
categories: [hobbies, domotics]
tags: [home, hass, domotics, esp]
redirect_from: /post/14
---

Since Apple realeased HomeKit I have been more and more interested in building a small brain for my house. I find it futuristic and fascinating.  

So here what I put together:

### Hardware

- 2 ESP8266: 2$ microcontrollers with embedded wifi;
- The Next Thing C.H.I.P;
- Raspberry Pi Zero W;
- WiFi enabled Lightbulb;
- WiFi enabled Power socket;
- External IP camera;
- Smart thermostat.

### Software

CHIP runs

- MQTT Server;
- PM2 (2 processes with some js code);
- Read data from ds18b20 sensor (OneWire);
- Fail2Ban.

RPI runs

- HassOS
  - Hass.io;
  - Web server to display informations;
  - HomeKit bridge and conversion of appliances data;
  - Presence detector.

ESP runs

- Arduino sketch that does the following:
  - Read data from DS18B20 sensor;
  - Send data to MQTT server.

Could it be simplified?  
Of course. But I bought them on different occasions and I just kept adding parts.

### Architecture

![Service Architecture](/images/posts/ha/arch.png)

I ditched Google Home in favor of a HomePod and Siri.. yeah, not quite there yet, but for now I'm happy with my choice. The only problem is: increadibly low number of supported appliances. Before 2018 HomeKit certification required Apple's approval and hardware implementation.  
Now it can be achieved via software, and the adoption is increasing. Slowly.

In my configuration, the Raspberry Pi is the main node. It runs and share the custom appliances to HomeKit (HomePod), which allows me to control them remotely via Apple's Home app.
To gather those informations, it connects to C.H.I.P. via MQTT, subscribing to the channels used by the thermometers. It also connects to the thermostat's gateway, lightbulb and power socket.

It runs a web server from which I can see and control the status.

![WebServer](/images/posts/ha/homepage.png)

### Sensors and communication

![Sensors and communication](/images/posts/ha/esp.png)

The standard seems to be [MQTT](http://mqtt.org).  
MQTT is a protocol designed to be fast and lightweight via publish/subscribe mechanism. The ESP8266 awakes from sleep, connects to the wifi and the MQTT server, reads the data from the temperature sensor and sends it over via a topic like `home/_room_/_sensor_`. Same thing for the sensor attached to the C.H.I.P., it simply routes the message to localhost.

The esp runs this sketch

<!-- {% gist da39e60125f9cec8a32fed857ce26175 %} -->


### Bridge to HomeKit

I am aware of 2 easy ways to bring unsupported/custom devices to homekit: homeassistant or Homebridge.
The first one wants to be the main-hub for everything inside your house, and has thousands of components ready-to-run. The second one is exactly what it looks like: a bridge between 3rd party appliances and HomeKit.

I used to prefer [Homebridge](https://github.com/nfarina/homebridge), but this time I decided to go with [homeassistant.io](https://homeassistant.io) because they recently changed their installation flow: now it's similar to what Raspberry Pi does with Raspbian, but Homeassistant calls it HassOS.

It's incredible how both solutions are simple to integrate with the Home app. The only necessary step is to scan or insert the code when prompted.

### Reliability

This was a bit of a tricky part. Outages in electricity and network are expected, and I really do not want to spend time checking what is or is not online.  
I have come across [PM2](https://pm2.io), a brilliant piece of software.

It's extremely easy to configure, it supports js and binaries. It has a nice `pm2 startup` command that generates a launch script to respawn all the currently-running apps. It has been extremely useful and if anything happens I have always seen the component brouhgt back to life and reconnected.  

![pm2 status](/images/posts/ha/pm2-status.png)

I also use the module _presence detection_ available in homeassistant to have a glance of the status of the other components. If they not home.. well, they are offline for some reason or I got burglarized.

![Presence](/images/posts/ha/presence.png)

### Next steps?

I only recently bought 2 ESP32, which they should be much more capable than the ESP8266. In the meantime I will change the sketch to support ultra-low energy consumption by the ESP8266, and try to leave it around. Would be nice to build a small case for it.

The only exception? Security devices.  
No way I will ever point a camera inside my home, and I will never ever buy "smart" locks. :)