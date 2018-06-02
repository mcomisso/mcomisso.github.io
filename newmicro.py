#!/usr/local/bin/python3

import subprocess
import sys
import os
import string
import datetime
import hashlib

DEFAULT_FOLDER = os.path.join(os.path.dirname(__file__), "_posts")
post_date = datetime.datetime.now()

template = """---
layout: micro
categories: ['micropost']
tags: ['microblog', 'thoughts']
date: '%s'
---
%s
"""

def md5_from_date(date):
  return hashlib.md5(bytes(str(date), 'utf-8')).hexdigest()

def create_file():
  """Create a file in the correct folder"""
  filename = "%s-%s.md" % (str(post_date.date()), md5_from_date(post_date.time()))
  return (open(os.path.join(DEFAULT_FOLDER, filename), "w+"), filename)


def write_post(file, content):
  """Write the post into a file"""
  file.write(template % (str(post_date.isoformat()), content))
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
  text =  ' '.join(sys.argv[1::])
  (file, filename) = create_file()
  write_post(file, text)
  save(filename)
  publish()