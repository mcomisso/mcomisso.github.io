---
layout: post
title: Manage ruby installations with rbenv
description: Quick commands to manage rubies
---

#### Install rbenv

Use **brew** as the default package manager in osx.
<!--more-->

```bash 
brew install rbenv rbenv-build
```

Append the following code to bash or zsh profile

```bash
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

#### Usage

Fetch the list of available ruby versions 

```bash
rbenv install -l
```

And install the desired one

```bash
rbenv install 2.3.0
```

Make it global

```bash
rbenv global 2.3.0
```

Or make it local. Every directory can have a local default ruby version.

```bash
rbenv local 2.3.0
```
