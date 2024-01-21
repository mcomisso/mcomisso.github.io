---
layout: post
title: MVVM Architecture
description: "MVVM architecture overview"
categories: [architecture, iOS]
tags: [iOS, mobile dev, arch, MVVM]
---

### MVVM

![MVVM graph](https://i-msdn.sec.s-msft.com/dynimg/IC416621.png)

**Model View ViewModel (Controller)**

[iOS ToDo implementation](https://github.com/mcomisso/todo-mvvm)

The _Controller_ is actually implicit.  
The code maintenance is helped by the new ViewModel entity, which keeps the actual logic to fetch the code from the model. In this way, the controller can be lighten from logic-specific management and specialized with almost pure view drawing methods.


### References
[iOS architecture patterns](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52#.hfbwmiarz)
