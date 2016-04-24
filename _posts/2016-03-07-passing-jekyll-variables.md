---
layout: post
title: Quick assign variables in jekyll
description: Syntax to assigning variables
categories: [web development]
tags: [github, jekyll, webdev]
---

### Quick assign variables in jekyll.

Square brackets seem to do the job correctly.

**Edit 2016-03-08**
- _Changed initial text for lower height in preview (blog page)._


This is how the `projects/index.html` page is built:
{% raw %}
```html
{%
  include projects.html
  project_title="Current projects"
  status="current"
%}
<div class="spacer"></div>
{%
  include projects.html
  project_title="Past projects"
  status="past"
%}
```

And this is the basic `project.html` template:

```html
[...]
  {% for project in site.data.projects.[include.status] %}
  <li>
    <span>
      <a href="{{project.site}}">
        <span>{{ project.name }}</span>
      </a>
      <span>
        {{ project.description }}
      </span>
    </span>
  </li>
  {% endfor %}
[...]
```

So, a inclusion can have parameters `{% include projects.html [...] status="current"%}` and you can include them right away with square brackets `{% for project in site.data.projects.[include.status] %}`.

{% endraw %}
