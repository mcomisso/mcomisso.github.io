---
layout: post
title: Sparkling sparkles
description: Make it rain
published: false
categories: [web development]
tags: [iOS, development, CoreAnimation]
comments: true
has_picture: true
---

## Kaboom

It was a while that I wondered about how various iOS applications implemented the sparkling effect (carousel).  
I decided to give it a look.

## Hello `CAEmitterLayer`, Hello `CAEmitterCell`

The idea is pretty straightforward, as the Apple APIs. Every particle you see coming to life is a `CAEmitterCell`, while the CAEmitterLayer is the canvas where those cells live.  
Writing as they have a life is not that bad, because, APIs speaking, these class do have exactly methods and properties as "birthRate" and "name".

<!-- ![]() insert image -->


## Implementing Sparkles

Let's start: [Download the base project](/projects/)

```swift
import UIKit
import QuartzCore

public class Sparkle: UIView {

    var emitter: CAEmitterLayer!

    required public init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }

    public override init(frame: CGRect) {
        super.init(frame: frame)
    }

    public func start() {
        emitter = CAEmitterLayer()

        emitter.emitterPosition = CGPoint(x: center.x, y: 0)
        emitter.emitterShape = kCAEmitterLayerLine
        emitter.emitterSize = CGSize(width: frame.size.width, height: 1)

        var cells = [CAEmitterCell]()

        cells.append(sparkleWithColor(UIColor.greenColor()))
        cells.append(sparkleWithColor(UIColor.blueColor()))
        cells.append(sparkleWithColor(UIColor.redColor()))

        emitter.emitterCells = cells
        self.layer.addSublayer(emitter)
    }


    public func stop() {
        emitter.birthRate = 0
    }

    func sparkleWithColor(color: UIColor) -> CAEmitterCell {
        let spark = CAEmitterCell()
        spark.name = "spark"
        spark.birthRate = 6.0
        spark.lifetime = 14.0
        spark.lifetimeRange = 0
        spark.color = color.CGColor
        spark.velocity = CGFloat(350.0)
        spark.velocityRange = CGFloat(80.0)
        spark.emissionLongitude = CGFloat(M_PI)
        spark.emissionRange = CGFloat(M_PI_4)
        spark.spin = CGFloat(3.5)
        spark.spinRange = CGFloat(4.0)
        spark.scaleRange = CGFloat(0.5)
        spark.scaleSpeed = CGFloat(-0.1)

        return spark
    }

}
```
