---
layout: page
title: Vinyly
description: A fresh view on Discogs
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

<meta name="apple-itunes-app" content="app-id=id1547173908">

<img style="width: 33%" src="/images/apps/Vinyly.png" alt="App icon"/>

> Vinyly is a Discogs client, built completely in SwiftUI.  
> It gives you a fresh view over your collection, and the ability to use Discogs' vast database.

#### [Download on appstore](https://apps.apple.com/gb/app/vinyly/id1547173908)

### A few screenshots

<div style="display: inline-grid; grid-template-columns: auto auto;">
  {% for image in page.images %}
  <div style="padding: 20px;">
    <img  src="{{ image.image_path }}" alt="{{ image.title}}"/>
  </div>
  {% endfor %}
</div>


[Privacy Policy](/vinyly/privacy-policy)