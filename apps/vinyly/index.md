---
layout: page
title: Vinyly
description: A fresh view on Discogs
appId: 1547173908
images:
  - image_path: /images/apps/vinyly/DetailDark.png
    title: Detail dark
  - image_path: /images/apps/vinyly/DetailLight.png
    title: Detail light
  - image_path: /images/apps/vinyly/LibraryView.png
    title: Library
  - image_path: /images/apps/vinyly/Search.png
    title: Search
---

<div style="display: inline-grid; grid-template-columns: auto auto;">

  <img style="width: 30%; border-radius: 18.625%;" src="/images/apps/Vinyly.png" alt="Vinyly App icon"/>

  <div>
  Vinyly is a <span><a href="https://discogs.com">Discogs</a></span> client, built completely in SwiftUI.<br/>
  It gives you a fresh view over your collection, and the ability to use Discogs' vast database.
  </div>

</div>
# Manage your Discogs collection

Vinyly connects to Discogs, and helps you manage your own collection.  
Add, remove, or move records between wantlist and your library.

# Find what's playing

Vinyly embeds Shazam! Let it listen what's playing to find your next record to hunt!

# Library insights

See how much is your collection is worth, and how well did your last few additions add to its value.

<a href="https://apps.apple.com/us/app/vinyly/id1547173908?itsct=apps_box_badge&amp;itscg=30200" style="display: inline-block; overflow: hidden; border-radius: 13px; width: 250px; height: 83px;"><img src="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83&amp;releaseDate=1613001600&h=b5f790a5f75a8aa8961bb3fc6a1f64b8" alt="Download on the App Store" style="border-radius: 13px; width: 250px; height: 83px;"></a>

# A few screenshots

<div style="display: inline-grid; grid-template-columns: auto auto;">
  {% for image in page.images %}
  <div style="padding: 20px; width: 60%;">
    <img  src="{{ image.image_path }}" alt="{{ image.title }}"/>
  </div>
  {% endfor %}
</div>

# Useful links

- [Privacy Policy](/vinyly/privacy-policy)
- [Medias](/vinyly/media.zip)

⚠️ Vinyly requires a discogs account