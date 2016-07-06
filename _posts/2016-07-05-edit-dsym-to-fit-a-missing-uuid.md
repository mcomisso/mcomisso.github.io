---
layout: post
title: "#10 - Fix Crashlytics missing dSYM"
description: "Edit a fresh dSYM to fit a build with a different UUID."
categories: [iOS]
tags: [iOS, otool, dsym, mobile dev]
redirect_from: /post/10
---

I was facing the following problem: AppStore with the latest production build and crashlytics without the corresponding dSYM file needed to symbolicate the crashes.  
What to do?

After some investigation, this is what I got from a freshly build dSYM:
- `LC_UUID` loads at the beginning of the binary file, with the command `1B`.
- Even if the architecture is litte endian, the UUID are written as big endian. This is a specification of the [UUID](http://www.ietf.org/rfc/rfc4122.txt): 
 

```C
[...]
    /* put name space ID in network byte order so it hashes the same
      no matter what endian machine we're on */
[...]
```
So:

1. Go back to the deploy commit, to make sure the build system will re-generate the app with the same symbols.

2. Archive again, with fastlane's gym or with a xcarchive  
        bin/gym # <- (I'm using bundler)

3. Get the current UUIDs  
        dwarfdump -u /path/to/MyApp.DSYM
        UUID: EBD9418E-20FF-44C1-8D3F-D7E75CC6F0B1 (armv7) MyApp.dSYM/Contents/Resources/DWARF/MyApp
        UUID: D9936E8B-139E-4F63-A063-7863EEFF6B99 (arm64) MyApp.dSYM/Contents/Resources/DWARF/MyApp

4. Change the UUIDs of the binary file with a hex editor.  
We are looking for the load command LC_UUID `1B000000` and we know that the command size is a 24 bytes long (or 0x18000000), followed by one of the UUIDs.  
Or, since arm is a little endian,`1B000000 18000000 XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX`, where XXXXXXXX are the bytes you may change with the correct UUID.

5. Save, submit, start bugfixing. :tada: