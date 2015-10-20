#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import scraperwiki

from format import item


def CleanTable(table_name, verbose=True):
  '''Clean all records from table in database.'''

  #
  # SQL statement.
  #
  print '%s Cleaning table `%s`.' % (item('bullet'), table_name)
  sql = 'delete from {table_name}'.format(table_name=table_name)

  #
  # SQL execution.
  #
  try:
    scraperwiki.sqlite.execute(sql)
    if verbose:
      print '%s Table `%s` cleaned successfully.' % (item('bullet'), table_name)

  except Exception as e:
    if verbose:
      print '%s Failed to clean table `%s`.' % (item('error'), table_name)
      print e
      return False



def StoreRecords(data, table):
  '''Store records in a ScraperWiki database.'''

  try:
    for record in data:
      scraperwiki.sqlite.save(record.keys(), record, table_name=table)

  except Exception as e:
    print "%s Failed to store record in database." % item('error')
    print e
    return False


def ReadAllRecords(table_name, verbose=True):
  '''Clean all records from table in database.'''

  #
  # SQL statement.
  #
  sql = 'select * from %s' % table_name

  #
  # SQL execution.
  #
  try:
    return scraperwiki.sqlite.execute(sql)['data']

  except Exception as e:
    if verbose:
      print '%s Failed to read table `%s`.' % (item('error'), table_name)
      print e
      return False
