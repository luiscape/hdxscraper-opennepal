#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from slugify import slugify
from unicodedata import normalize

def Date(record):
  '''Patching date stamps.'''

  a = time.strptime(record, '%b %d, %Y')
  b = time.strftime('%m/%d/%Y', a)
  return b


def Slug(text):
  '''Slugiffy strings of text.'''

  try:
    return slugify(text)[0:90]

  except Exception as e:
    print 'Failed to patch data.'
    print e
