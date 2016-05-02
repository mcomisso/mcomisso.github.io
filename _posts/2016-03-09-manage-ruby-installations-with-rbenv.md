---
layout: post
title: Manage ruby installations with rbenv
description: Quick commands to manage rubies
categories: [system administration]
tags: [ruby, rbenv, zsh]
---

### Install rbenv

Use **brew** as the default package manager in osx.

```bash
brew install rbenv rbenv-build
```

Append the following code to bash or zsh profile to initialize the `rbenv` command.

```bash
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Usage


**List**   
Fetch the list of available ruby versions

```bash
rbenv install -l
```

**Install**   
Install the desired one

```bash
rbenv install 2.3.0
```

**Global**  
Make it the default installation global

```bash
rbenv global 2.3.0
```

**Local**  
Or make it local. Each directory can have a local default ruby version.

```bash
rbenv local 2.3.0
```
