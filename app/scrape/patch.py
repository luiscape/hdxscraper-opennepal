#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from unicodedata import normalize

def Date(data):
  '''Patching date stamps.'''

  for record in data:
    m = time.strptime(record['month_en'], '%B')
    m = time.strftime('%m', m)
    record['date'] = '{year}-{month}'.format(year=record['year'], month=m)

  return data


def Slug(text):
  '''Slugiffy strings of text.'''

  text = text.lower().replace(' ', '-')
  return text
