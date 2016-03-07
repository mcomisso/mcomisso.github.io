---
layout: post
title: Quick assign variables in jekyll
description: Syntax to assigning variables
categories: [web development]
tags: [github, jekyll, webdev]
---

## Quick assign variables in jekyll

Ever wanted to pass a variable to a template, while using its name to determine which array to loop?
Square brackets seem to do the job correctly.

This is how the `projects/index.html` page is built:

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
  {% for project in site.projects.[include.status] %}
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

So, a inclusion can have parameters `{% include projects.html [...] status="current"%}` and you can include them right away with square brackets `{% for project in site.projects.[include.status] %}`.
