---
layout: post
title: "July 30, '24 - Chemo Infusion #4 of 6"
categories:
  - Life
  - Cancer
  - Cancer Update
tags:
  - Cancer
excerpt: PSA ???! The return of the Karen.
---
- PSA: ????! 
- Support: Karen parte deux!

## Day 0 of cycle : injection

## Day 1 of cycle

## Day 2 of cycle


## Day 3 of cycle

## Day 4 of cycle


## Day 5 of cycle


## Day 6 of cycle

## Day 7 of cycle (final shot)

## Other things to mention


{% assign posts = site.posts | where_exp: "item", "item.title contains '4 of 6'" %}

{% if posts.size > 0 %}
## Next Update:  

  {% for post in posts %}
[{{ post.title }}]({{ post.url }})
  {% endfor %}
{% endif %}
