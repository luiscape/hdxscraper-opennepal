#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def Date(data):
  '''Patching date stamps.'''

  for record in data:
    m = time.strptime(record['month_en'], '%B')
    m = time.strftime('%m', m)
    record['date'] = '{year}-{month}'.format(year=record['year'], month=m)

  return data
