---
layout: post
title: 5 Most useful plugins in Xcode
description: A list of useful plugins for Xcode 7
published: true
categories: [Xcode, iOS development]
tags: [iOS, Xcode, ]
comments: true
has_picture: true
---

Xcode is great tool --when does not crashes--, but with these it really becomes super efficient.


## Alcatraz  

<img class="max-width" src="http://alcatraz.io/images/screenshot@2x.png"/>

Well, this is essential. Simplifies a lot the install/uninstall passage for almost any other plugin or extension.  
Download it by copying this into a new terminal window:

```bash
curl -fsSL https://raw.githubusercontent.com/supermarin/Alcatraz/deploy/Scripts/install.sh | sh
```

## GitDiff

![GitDiff Image](https://raw.github.com/onevcat/VVDocumenter-Xcode/master/ScreenShot.gif)

Highlights every line has changed since the last commit. It is also possible to reset the highlighted lines or just find out what was written there before the editing.

## VVDocumenter-Xcode

![VVDocumenter Image](http://injectionforxcode.johnholdsworth.com/gitdiff2.png)

Keeping your code documented? So annoying without this.  
Just enter `///` over one of your classes, methods definition, variables to get the Xcode supported documented section.

## KSImageNamed

![KSImageNamed Image](https://raw.github.com/ksuther/KSImageNamed-Xcode/master/screenshot.gif)

How many times do you forget about the name of that image in xcassets?  
With KSImageNamed you get for free a list + preview of the stored images. Just start typing `[UIImage imageNamed]`.

## Autoindent with save

![Autoindent Image](https://github.com/ThilinaHewagama/AutoIndentWithSave/blob/master/auto_indent_screen_shot.jpg)

If you get annoyed by not having code correctly in-line, this is the right plugin to install.  
It checks and re-indent all the code every time you press `cmd + S`. With small displays sometimes the view scrolls around, but it happens only the first time this plugin sees the file you are saving.
