---
layout: page
title: About
description: About page
---

# Hello

I'm an italian software developer based in [London](https://goo.gl/maps/qSTGhQfBvbS2){:target="_blank"}, :uk:.

{% avatar mcomisso size=500 %}

I work for YNAP, as Senior iOS developer in "The Outnet" iOS team.

{% assign post = site.posts | where: "layout","post" | first %}
{% assign tags_sentence = post.tags | sort | array_to_sentence_string %}
Recently I posted something about {{ tags_sentence }}: [{{ post.title }}]({{ post.url }}).

### Want to get in touch? 

[Send me an email](mailto:{{ site.email }})

or  

<p>
{% for service in site.about.services %}
  <a style="display: inline-block; width: 2em;" href="{{ service.url }}"><i id="{{ service.name | slugify }}" class="fab fa-2x fa-{{ service.name }}"></i> </a>
{% endfor %}
</p>

### I was involved in the making of these apps:

<p>
{% for app in site.data.works reversed %}
  <a href="{{ app.url }}" style="display: inline-block; width: 4em;">
    <img title="{{ app.name }}" alt="{{ app.name }} icon" src="{{ site.url | append: app.icon }}"  style="border-radius: 15.625%; width:100px; border: 1px; border-color: #ccc; border-style: solid;" />
  </a>
{% endfor %}
</p>

### And I have a couple of open source repositories too

{% for proj in site.data.github %}
  <span id="id{{ proj.name }}" style="text-align: center;">
    <a href="{{ proj.url }}">{{proj.name}}</a> - {{ proj.description }}
  </span>
{% endfor %}
