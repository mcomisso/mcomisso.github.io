--- 
layout: page 
title: About 
description: About page 
---

# Hello

I'm a iOS developer in <a href="https://goo.gl/maps/qSTGhQfBvbS2" target="_blank"> London. </a>

![ProfileImage]("https://twitter.com/"{{ site.about.services[1].username | remove: ' @
' }}/profile_image?size=original")
          
My current interests are Swift development and AR applications, but I constantly stay updated with the latest technologies, trying them myself as soon as possible.
          
Recently I posted something about {% assign post = site.posts | first %} {{ post.tags | sort | array_to_sentence_string }}: <a href="{{ post.url }}">{{ post.title }}</a> 

### I was involved in the making of these apps:

<table>
<thead>

</thead>
<tr>
  <th>
    App
  </th>
  <th>
    Description
  </th>
  <th>
    url
  </th>
</tr>
{% for app in site.data.works %}
  <tr>
    <td>
      <a href="{{ app.url }}">
        <img src="{{ site.url }}{{ app.icon }}" alt="{{ app.name }} icon" style="border-radius: 15.625%;" />
      </a>
    </td>
    
    <td>
      <div for="id{{ app.name }}">
        {{ app.description }}
      </div>
    </td>

    <td>
      <p id="id{{app.name}}" style="text-align: center;">
        <a href="{{ app.url }}">{{app.name}}</a>
      </p>
    </td>
  </tr>
{% endfor %}
</table>

### And I have a couple of open source repositories too

{% for proj in site.data.github %}
  <span id="id{{ proj.name }}" style="text-align: center;"><a href="{{ proj.url }}">{{proj.name}}</a> - {{ proj.description }}</span>
{% endfor %}


### Want to get in touch? 

<a href="/contact">Send me an email</a> or use Intercom by pressing the bottom right button on this page.

{% for service in site.about.services %}
<a href="{{ service.url }}">
  <i id="{{ service.name | slugify }}" class="fa fa-{{ service.name }}"></i>
  <span class="mdl-chip__text">{{ service.name }}</span>
</a>
{% endfor %}