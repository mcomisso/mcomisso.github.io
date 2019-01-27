---
layout: post
title: "#13 - Protocols and delegates"
description: "Protcols and delegates"
categories: [development, iOS]
tags: [mobile dev, iOS]
redirect_from: /post/13
---

At The Outnet we decided it would be a good idea to organize a weekly meetup about iOS tech, to share ideas, experiences, and anything that the more junior members would like to rehash.  

One good question I got was about Protocols and Delegates:  
how do we use them and how do they differ?

Let's start by highlighting the difference, focusing on iOS.

> A Protocol is a components of the Swift (or Obj-C) programming language  
> A Delegate is the implementation of the Delegation Pattern (Object Oriented Programming)

A small refresher for the Objective-C syntax and Swift:

```obj-c
// Objective C
@protocol MyProtocol

// properties and methods signatures

@end
```

```swift
// Swift
protocol MyProtocol { }
```

---

# Protocols define behaviors and characteristics that will be implemented by another class, struct or enum

This might include variables or methods signatures:

``` swift
protocol Themable {
  var themeColor: UIColor { get }
  func set(color: UIColor)
}

extension UILabel: Themable {

  var themeColor: UIColor {
    return self.textColor
  }

  func set(color: UIColor) {
    self.textColor = color
  }
}

let label = UILabel()
label.set(color: .green)
label.themeColor // UIColor.green
```


# Delegates often use protocols to achieve Dependency inversion (SOLI**D** principles).

> Delegation pattern: An object handles a request by delegating it to a second object

A very common example is the `UITableViewDelegate` protocol:  
we declare a new class or implement it directy on the UIViewController, and extend that protocol's methods to allow the tableview to use it as its own delegate.

```swift
class MyTableViewDelegate: NSObject, UITableViewDelegate {

  // This is a method declared inside UITableViewDelegate, required for us to be implemented.
  func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    { ... Do something ...  }
  }
}

class MyViewController: UIViewController {

  @IBOutlet weak var tableView = UITableView!

  let myTableViewDelegate = MyTableViewDelegate()

  override func viewDidLoad() {
    super.viewDidLoad()
    // { ... }
    tableView.delegate = self.myTableViewDelegate
  }
}
```

---

# POP (Protocol Oriented Programming)

This is a new concept that for us iOS developers came with Swift.  
Very good videos from past WWDCs are available here:

- [2015 - Session 408: Protocol-Oriented Programming in Swift](http://devstreaming.apple.com/videos/wwdc/2015/408509vyudbqvts/408/408_hd_protocoloriented_programming_in_swift.mp4)
- [2016 - Session 419: Protocol and Value oriented programming in UIKit apps](http://devstreaming.apple.com/videos/wwdc/2016/419lgbsyhjrmqtmq0qh/419/419_hd_protocol_and_value_oriented_programming_in_uikit_apps.mp4)
- [2018 - Session 406: Swift Generics](https://devstreaming-cdn.apple.com/videos/wwdc/2018/406z8wpyv2jdenet9rc/406/406_hd_swift_generics.mp4)

This brings the concept of composition over Inheritance: avoid subclassing, use protocols to focus on single, small functionalities and compose a new complex object by merging them together.

We can give a standard implementation for each protocol

```swift
protocol Movable {
    func move()
}

protocol HasSpeakAbility {
    func talk()
}

protocol HasWalkAbility {
    func walk()
}

protocol HasRunAbility: HasWalkAbility {
    func run()
}
```

# Use protocol extensions

A protocol extension is an useful way to share a common implementation between al objects that extend the same protocol.
In this example we have an extension for each protocol that simply prints out the action of its main defining method.  
If we would ever need a more specific implementation, nothing stops up to implement that method directly from the object struct/enum/class that extends the protocol.

```swift
extension Movable {
    func move() { print("I'm moving") }
}

extension HasWalkAbility {
    func walk() { print("\(String(describing: self)): I'm walking") }
}

extension HasRunAbility {
    func run() { walk(); print("....faster") }
}

extension HasWalkAbility where Self: Movable {
    func walk() { print("I'm walking") }
}

struct Hero: HasRunAbility, HasSpeakAbility {
    let name: String

    func talk() {
        print("oh s**t!")
    }
}

struct Zombie: HasWalkAbility, HasSpeakAbility {
    func talk() {
        print("GAAARGH")
    }
}


let zombie = Zombie()
let hero = Hero(name: "Hero")

zombie.walk()
hero.walk()

zombie.talk()
hero.talk()

hero.run()
```

# Use protocol composition

Sometimes it's easy to identify behaviors that can be logically linked together. We might want a shortcut to call all the hero actions, or all the zombie actions. Or maybe we want to have a collection of objects that share the same multiple behaviors, like `run()`.

```swift
typealias HeroActions = HasRunAbility & HasSpeakAbility & Movable
typealias ZombieActions = HasWalkAbility & HasSpeakAbility & Movable

extension String {
    var mutableString: NSMutableAttributedString {
        return NSMutableAttributedString(string: self)
    }
}
```

Composition comes really handy when we want to declare some method optional. Let's focus on `UITableViewControllerDataSource`, this is taken from the header file of `UITableView`.

```objective-c
@protocol UITableViewDataSource<NSObject>

@required
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section;

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath;

@optional
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView;

- (nullable NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section;

{...}
```

We see the `@required` and `@optional` attributes preceeding those methods. They declare which ones have to be implemented and which ones can be left out.

We could achieve a similar result by using protocol composition: one protocol will contain the optional methods, the other one the required.

```swift
protocol UITableViewRequiredDataSource {
  func tableView(_ tableView: UITableView, numberOfRows section:NSInteger)

  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath)
}

protocol UITableViewOptionalDataSource {
  func numberOfSections(_ tableView: UITableView)
  func tableView(_ tableView: UITableView, titleForHeader section: Int)
}
```

And then composing a new type depending on what behavior we need:

```swift

class MyViewController {
  @IBOutlet weak var tableView: UITableView!

  private var tableViewDataSource: UITableViewRequiredDataSource

  // or
  
  private var tableViewDataSource: UITableViewRequiredDataSource & UITableViewOptionalDataSource
}
```

I hope this might help as a reference :)