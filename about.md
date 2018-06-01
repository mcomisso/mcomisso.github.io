--- 
layout: page 
title: About 
description: About page 
---

# Hello

I'm a iOS developer in <a href="https://goo.gl/maps/qSTGhQfBvbS2" target="_blank"> London. </a>

![ProfileImage](https://twitter.com/{{ site.about.services[1].username | remove: '@' }}/profile_image?size=original)
          
I do enjoy My current interests are server-side Swift and AR applications, but I constantly stay updated with the latest technologies, trying them myself as soon as possible.
          
Recently I posted something about {% assign post = site.posts | first %} {{ post.tags | sort | array_to_sentence_string }}: <a href="{{ post.url }}">{{ post.title }}</a>

### Want to get in touch? 

Send me an email: matteo.comisso -at- icloud.com  
or  
<p>
{% for service in site.about.services %}
  <a style="display: inline-block; width: 2em;" href="{{ service.url }}"><i id="{{ service.name | slugify }}" class="fa fa-2x fa-{{ service.name }}"></i> </a>
{% endfor %}
</p>
{% include styles.html %}

### I was involved in the making of these apps:

<table>
<thead>

</thead>
<tr>
  <th> App </th>
  <th> Description </th>
  <th> url </th>
</tr>
{% for app in site.data.works reversed %}
  <tr>
    <td>
      <a href="{{ app.url }}">
        <img src="{{ site.url | append: app.icon }}" alt="{{ app.name }} icon" style="border-radius: 15.625%;" />
      </a>
    </td>
    <td>
      <p for="id{{ app.name }}">
        {{ app.description }}
      </p>
    </td>
    <td>
      <p id="id{{ app.name }}">
        <a href="{{ app.url }}">{{ app.name }}</a>
      </p>
    </td>
  </tr>
{% endfor %}
</table>

### And I have a couple of open source repositories too

{% for proj in site.data.github %}
  <span id="id{{ proj.name }}" style="text-align: center;">
    <a href="{{ proj.url }}">{{proj.name}}</a> - {{ proj.description }}
  </span>
{% endfor %}