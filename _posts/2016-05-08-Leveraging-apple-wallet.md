---
layout: post
title: "#8 - Leveraging Apple Wallet"
description: "Creating a personal pass-badge with iBeacon integration"
categories: [iOS]
tags: [iOS, mobile dev, passbook, iBeacons]
redirect_from: /post/8
---

### Preparing for WWDC

Since I'm kinda a social awkward guy, I've decided to create a little pass for the iOS Wallet. The idea is to share it online, and make it pop onto the display when someone is getting close to me, just to say "Hi" and/or share contact information.  
A standalone application to distribute would be a dumb choice to make, since no one wants to keep a cv in their precious homescreen... but  wallet and its passes can come in handy.  
iBeacons are also silently issued by iOS, and such a not-so-much-known-functionality is inside passbook since iOS7.


Making passes is super easy. A pass is just a `json` file, with a bunch of predefined images inside a directory named **_any_.pass**, plus the signing command `signpass` which sits in your $PATH since XCode installation.

Only a short number of keys are required on the first json level:

| key name | Type | Description |
|----------|------|-------------|
| description | localizable string | Required. Brief description of the pass, used by the iOS accessibility technologies. Don’t try to include all of the data on the pass in its description, just include enough detail to distinguish passes of the same type.
| formatVersion | integer | Required. Version of the file format. The value must be 1.
| organizationName | localizable string | Required. Display name of the organization that originated and signed the pass.
| passTypeIdentifier | string |  Required. Pass type identifier, as issued by Apple. The value must correspond with your signing certificate.
| serialNumber |string |  Required. Serial number that uniquely identifies the pass. No two passes with the same pass type identifier may have the same serial number.
| teamIdentifier | string | Required. Team identifier of the organization that originated and signed the pass, as issued by Apple.

```json
{
  "description": "Matteo Comisso",
  "formatVersion": 1,
  "organizationName": "Matteo Comisso",
  "passTypeIdentifier": "pass.reverse.dns",
  "serialNumber": " take the latest group of digits from `uuidgen` ",
  "teamIdentifier": " *redacted* ",
  "..." : "...",
}
```

But we can add more keys to personalize it. It will kinda match this site palette, just for a bit of consistency.

```json
{
  "..." : "...",
  "logoText": "Matteo Comisso",
  "labelColor": "rgb(206, 215, 219)",
  "foregroundColor": "rgb(255, 255, 255)",
  "backgroundColor": "rgb(95, 125, 138)",
  "..." : "..."
}
```

And finally the beacon section:

| key name | Type | Description |
|----------|------|-------------|
| major | 16-bit unsigned integer | Optional. Major identifier of a Bluetooth Low Energy location beacon.
| minor | 16-bit unsigned integer | Optional. Minor identifier of a Bluetooth Low Energy location beacon.
| proximityUUID | string | Required. Unique identifier of a Bluetooth Low Energy location beacon.
| relevantText | string | Optional. Text displayed on the lock screen when the pass is currently relevant. For example, a description of the nearby location such as “Store nearby on 1st and Main.”


```json
{
  "..." : "...",
  "beacons": [{
    "proximityUUID": "96A1736B-11FC-85C3-1762-80DF658F0B29",
    "relevantText": "Matteo salutes you 👋"
  }],
  "..." : "...",
}
```

iOS will take care to scan for geofencing regions, and display it on the lockscreen when inside one.
And yes, emojis. :tada:


The full `pass.json` here following:

```json
{
    "formatVersion": 1,
    "passTypeIdentifier": "pass.reverse.dns",
    "serialNumber": " *call uuidgen* ",
    "logoText": "Matteo Comisso",
    "teamIdentifier": " *redacted* ",
    "organizationName": "Matteo Comisso",
    "description": "Matteo Comisso",
    "labelColor": "rgb(206, 215, 219)",
    "foregroundColor": "rgb(255, 255, 255)",
    "backgroundColor": "rgb(95, 125, 138)",
    "beacons": [{
        "proximityUUID": "CD8FA7EE-3847-42E0-A717-24EDC9CD33D8",
        "relevantText": "Matteo salutes you 👋"
    }],
    "barcode": {
      "altText" : "http://mcomisso.xyz/about",
      "format" : "PKBarcodeFormatQR",
      "message" : "http://mcomisso.xyz/about",
      "messageEncoding" : "iso-8859-1"
    },
    "generic": {
        "primaryFields": [{
            "key": "work_desc",
            "label": "",
            "value": "iOS/web Developer",
        }],
        "secondaryFields": [{
            "key": "website",
            "label": "Website",
            "value": "http://mcomisso.xyz",
        }],
        "auxiliaryFields": [{
            "key": "email",
            "label": "email",
            "value": "matteo.comisso@me.com"
        }, {
            "key": "twitter",
            "label": "Twitter",
            "value": "@teomatteo89"
        }],
        "backFields": [{
            "key": "name_back",
            "label": "whoami",
            "value": "Matteo Comisso"
        }, {
            "key": "email_back",
            "label": "reply",
            "value": "matteo.comisso@me.com"
        }, {
            "key": "website_back",
            "label": "Website",
            "value": "http://mcomisso.xyz/about",
            "dataDetectorTypes": [
                "PKDataDetectorTypeLink"
            ]
        }, {
            "key": "location_back",
            "label": "Where?",
            "value": "Venice, Italy",
            "dataDetectorTypes": [
                "PKDataDetectorTypeAddress"
            ]
        }]
    }
}
```

The directory structure will have this hierarchy:

```bash
mcomisso.pass
├── icon.png
├── icon@2x.png
├── logo.png
├── logo@2x.png
├── pass.json
├── thumbnail.png
└── thumbnail@2x.png
```

And the latest thing to do is call `signpass` with the **-p** option.

```bash
signpass -p mcomisso.pass
```

### About testing

You have to send it via email or downloading with http to your device.  
I preferred starting up MAMP, putting it in a new folder inside htdocs and doing a

```bash
echo '<html><body><a href="./mcomisso.pkpass">DOWNLOAD PASS</a></body></html>' > index.html
```

Tap, add, done. :rocket:

### Final result
![Lockscreen Image](http://res.cloudinary.com/dmsmziyvz/image/upload/c_scale,w_365/v1462646561/IMG_3049_o2ku04.png) 

![Wallet Image](http://res.cloudinary.com/dmsmziyvz/image/upload/c_scale,w_365/v1462646559/IMG_3047_gz5ras.png)


### References
* [Passkit -  Reference](https://developer.apple.com/library/ios/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012026-CH0-SW1)
* [Wallet programming](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
* [iBeacon](https://en.wikipedia.org/wiki/IBeacon)
* [Wikibeacon - radius networks](http://wikibeacon.org/map)
