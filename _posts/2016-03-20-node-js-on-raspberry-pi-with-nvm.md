---
layout: post
title: Node.js with nvm
description: "How to install Node.js with nvm"
categories: [Nodejs, hotwo]
tags: ["Raspberry pi", "Raspi", "howto", "nvm", "nodejs"]
---

### Node Version Manager
Manual install:

```bash
$ git clone https://github.com/creationix/nvm.git ~/.nvm && cd ~/.nvm && git checkout v0.31.0
$ echo "source ~/.nvm/nvm.sh" >> ~/.zshrc
$ source ~/.zshrc
```
Check if works:

```bash
$ nvm --version
0.31.0
```

### Install Node.js

Get a list of available installations:

```bash
$ nvm ls-remote
[...]
v5.7.1
v5.8.0
v5.9.0
```
**Install Node**

```bash
$ nvm install v5.9.0
```

**Check**

```bash
$ node -v
```
