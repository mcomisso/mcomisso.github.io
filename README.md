# mcomisso.github.io
[![Build Status](https://travis-ci.org/mcomisso/mcomisso.github.io.svg?branch=master)](https://travis-ci.org/mcomisso/mcomisso.github.io)
[![License](http://img.shields.io/:license-gpl3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Code Climate](https://codeclimate.com/github/mcomisso/mcomisso.github.io/badges/gpa.svg)](https://codeclimate.com/github/mcomisso/mcomisso.github.io)
[![Issue Count](https://codeclimate.com/github/mcomisso/mcomisso.github.io/badges/issue_count.svg)](https://codeclimate.com/github/mcomisso/mcomisso.github.io)

Hey there.  
This is the personal site/blog of Matteo Comisso.  


## Libraries and tools
- Created using [Google's Material Design Lite](https://www.getmdl.io) (Released under Apache 2 license).
- [Travis-ci](https://travis-ci.org "Travis-ci") for continuous integration.


## FAQ
###### Creating a post?  
Create file as `_posts/YEAR-MONTH-DAY-title.MARKUP`.

###### Starting a draft?  
Create file as `_drafts/YEAR-MONTH-DAY-title.MARKUP`.

###### Publishing?  
Move from _drafts to _posts and `add, commit & push`.


## Site structure

There's 4 types of pages:

- error.html  
  Template for error pages

- default.html  
  The base site structure. (Body, header, side menu, etc)

  - page.html  
    A base structure for any page, not related to posts.

  - post.html  
    Template for any post.

## Includes

I tried to modularize the components, by splitting macro html-blocks into their own files.


## License and attribution
- All contents of this site are under CC,
[Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)

- All development related files and structure are under [GNU General Public License v3.0](http://www.gnu.org/licenses/gpl-3.0.en.html)

- Libraries are under their own License and attribution, check before use.
