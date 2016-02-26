---
layout: post
title: Base installation of Raspberry Pi
description: Little TODO list to setup a Raspberry Pi
published: true
categories: [raspberry pi]
tags: [raspi, ssh, howto]
comments: true
has_picture: true
---

Basic steps to setup a Raspberry Pi.
------------------------------------

#### Installation Quick List
1. Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/ "Download Raspbian"). Jessie is the latest stable at the moment, based on debian.
<!--more-->

2. Unzip it and write it down to a sdcard.  
```
sudo dd if='/path/to/file.img' of='/dev/sdcard' bs=1024
```

3. Boot! Attach network cable, sdcard, power. :tada:

#### Make it yours
After the installation, it is highly suggested to change the basic auth for accessing the pi.

- Change the password  
You definitely do not want the default password to access a passwd-less sudo account.  
```
$ sudo passwd pi
```

- Increase ssh security  
The */etc/ssh/ssd_config* file contains all the configurations for the ssh daemon.  

  - Change auth method (repeat step 1-2-3 for every machine, use always different keys for each one)  
  PASSWORDS ARE BAD.  
    1. Do a `ssh-keygen -t rsa -b 4096` on the host machine and follow the instructions to generate a new key.  

    2. Copy the freshly generated public key  

            $ cat .ssh/id_rsa.pub | pbcopy

    3. Add it to the raspi authorized keys

            $ sudo nano .ssh/authorized_keys

    4. Edit the *sshd_config* _PasswordAuthentication_ parameter  

            $ sudo nano /etc/ssh/sshd_config
            [...]
            PasswordAuthentication no
            [...]

    5. Restart ssh

        sudo service ssh restart


  - Change default sshd port

    1. Edit the *ssd_config* _Port_

        $ sudo nano /etc/sshd_config
        # Package generated configuration file  
        # See the sshd_config(5) manpage for details  
        # What ports, IPs and protocols we listen for
        Port 1234

    2. Restart ssh

        sudo service ssh restart
