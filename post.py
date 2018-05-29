#!/usr/local/bin/python

import subprocess
import sys
import os
import string
import datetime

DEFAULT_FOLDER = os.path.join(os.path.dirname(__file__), "_posts")

template = """---
layout: micro
categories: [micropost]
tags: [microblog, thoughts]
---
%s
"""


def create_file():
  """Create a file in the correct folder"""
  filename = "%s.md" % str(datetime.datetime.now()).replace(' ', '-')
  return (open(os.path.join(DEFAULT_FOLDER, filename), "w+"), filename)
  

def write_post(file, content):
  """Write the post into a file"""
  file.write(template % content)
  file.close()

def save(filename):
  """Save the commit inside the repository"""
  git_add_output = subprocess.check_output(["git", "add", "./*"])
  print(git_add_output)

  git_commit_output = subprocess.check_output(["git", "commit", "-am", "[Micro] %s" % filename])
  print(git_commit_output)

def publish():
  git_push = subprocess.check_output(["git", "push"])
  print(git_push)



if __name__ == '__main__':
  text =  string.join(sys.argv[1::])
  (file, filename) = create_file()
  write_post(file, text)
  save(filename)
  publish()