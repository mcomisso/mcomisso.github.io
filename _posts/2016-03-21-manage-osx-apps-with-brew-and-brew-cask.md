---
layout: post
title: Manage osx apps with brew and brew cask
description: Brew is the new standard package manager for osx
categories: [quicklist, macosx, brew]
tags: ['quicklist', 'list', 'howto', 'brew', 'macosx']
---

### Brew

**Kickstart**  
[Brew](http://brew.sh/) is a modern, fast and full-featured package manager for OSX.

**Brew installation**

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

**Detect current configuration problems**  
Brew will list any issue and suggestion about how to fix it.

```bash
$ brew doctor
```

### Basic usage

**Search for software**

```bash
$ brew search wget
```


**Install software**

```bash
$ brew install wget
```


**Delete software**

```bash
$ brew rm wget
```


**Update brew, upgrade formulas, clean older and cache**

```bash
$ brew update && brew upgrade && brew cleanup
```

---------------


### Brew cask

_Brew cask_ is now integrated with _Brew_. It manages graphical software, by installing it in `/opt/Homebrew-cask/Caskroom/` and linking the apps to `~/Applications/`.
More info available here: [Homebrew Cask](https://github.com/caskroom/homebrew-cask)

**Search**  

```bash
$ brew cask search slack
```


**Install**

```bash
$ brew cask install slack
```

**Remove**

```bash
$ brew cask rm slack
```

**Completely uninstall**

```bash
$ brew cask zap slack
```


**Clean**

```bash
$ brew cask cleanup
```
