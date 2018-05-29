#!/usr/local/bin/python

import subprocess
import sys
import os
import string
import datetime

DEFAULT_FOLDER = os.path.join(os.path.dirname(__file__), "_posts")


template = """---
layout: micro
categories: [microblog]
tags: [microblog, thoughts]
---
%s
"""

def create_file():
  filename = str(datetime.datetime.now()).replace(' ', '-')
  return (open(os.path.join(DEFAULT_FOLDER, filename), "w+"), filename)
  

def write_post(file, content):
  file.write(template % content)
  file.close()



def publish(filename):
  git_add_output = subprocess.check_output(["git", "add", "./*"])
  output = subprocess.check_output(["git", "commit", "-am", filename])
  print(output)



if __name__ == '__main__':
  text =  string.join(sys.argv[1::])
  (file, filename) = create_file()
  write_post(file, text)
  publish(filename)