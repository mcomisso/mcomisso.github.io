---
layout: post
title: "#12 - SQFeedbackGenerator"
description: "UINotificationFeedbackGenerator on iPhone 6S"
categories: [development, iOS]
tags: [mobile dev, iOS]
redirect_from: /post/12
---

# SQFeedbackGenerator 📳

#### [Available on github <i class="fab fa-github"></i>](https://github.com/mcomisso/SQFeedbackGenerator)

I'm spending my weekends building my app called [Squirrel](http://squirrelapp.rocks), and I wrote a simple class to take advantage of `AudioServicesPlaySystemSound` to provide an haptic vibration for certain scenarios (error, success, notification).

I noticed this functionality thanks to [Bear](http://www.bear-writer.com), an amazing note taking app (which btw, is made in 🇮🇹!)

:+1: 

Give it a spin on your device with:

```ruby
pod try SQFeedbackGenerator
```

or add this to your Podfile:

```ruby
pod 'SQFeedbackGenerator'
```
