---
layout: post
title: "#9 - Synced countdown"
description: "One project a day: Synced countdown between two clients"
categories: [webdev]
tags: [nodejs, socket.io]
redirect_from: /post/9
---

> Long distance relation but still want to watch a movie together?  

Here comes [Syncstart](https://syncstart.herokuapp.com)!

Last week I decided to build a synced timer between two web clients, without actually spend more then an afternoon on it.  

The idea behind is pretty simple:  

* first client opens the webapp and receives a code
* second client opens the webapp and enters the code.  

Oh, and you find yourself playing *rock-paper-scissors-lizard-spock* too.

Since I need some data persistency and a free hosting service, I chose [Heroku](https://heroku.com) + [mLab](https://mlab.com/) mongodb instance.  
Heroku solutions are really became pretty neat for this kind of super-quick prototyping/ideas. :rocket:  
The code is available on github.

##### References
* [Syncstart](https://syncstart.herokuapp.com)
* Git repository: [Syncstart repo](https://github.com/mcomisso/Syncstart)
* Socket.io emit list: [Actually I saved a snippet here](/post/7)
