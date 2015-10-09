#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import schedule
import app.main as App
from app.utilities.format import item

#
# Setting-up schedule.
#
schedule.every(30).seconds.do(App.Main)

def Main(verbose=True):
  '''Wrapper to run all the scheduled tasks.'''

  if verbose:
    print '%s Running scheduler.' % item('bullet')

  try:
    while True:
      schedule.run_pending()
      time.sleep(1)

  except Exception as e:
    print e
    return False


if __name__ == '__main__':
  Main()
