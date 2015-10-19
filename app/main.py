#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import scraperwiki
import scrape.patch as Patcher
import scrape.scrape as Scraper

from utilities.format import item
from utilities.db import CleanTable, StoreRecords
from scrape.export import ExportDatasets,ExportResources

__version__ = 'v.0.2.0'

def Collect():
  '''Scrapes and stores data in database.'''

  #
  # Collecting URLs from OpenNepal.
  #
  print '%s Collecting dataset URLs from OpenNepal.' % item('bullet')

  urls = []
  for page in range(0, 5):
    data = Scraper.ScrapeURLs(page=page)
    urls += data

  #
  # Storing URLs.
  #
  CleanTable('opennepal_urls')
  StoreRecords(urls, 'opennepal_urls')


  #
  # Scrape content.
  #
  errors = 0
  content = []
  print '%s Scraping datasets.' % item('bullet')
  for url in urls:
    try:
      c = Scraper.ScrapeContent(url=url['url'])
      content.append(c)

    except Exception as e:
      errors += 1
      print '%s Error scraping dataset: %s' % (item('error'), url['url'])


  print '%s There were a total of %s error(s) scraping data.'  % (item('warn'), str(errors))

  #
  # Storing content.
  #
  CleanTable('opennepal_content')
  StoreRecords(content, 'opennepal_content')

  print '%s Collected data from OpenNepal successfully.\n' % item('success')

  return content


def Patch(data):
  '''Patching data.'''
  print '%s Patching data.' % item('bullet')

  out = []
  for record in data:
    record['id'] = Patcher.Slug(record['title'])
    record['dataset_date'] = Patcher.Date(record['date'])
    out.append(record)


  #
  # Storing content.
  #
  CleanTable('opennepal_content')
  StoreRecords(out, 'opennepal_content')
  print '%s Patched data successfully.\n' % item('success')

  return out


def ExportJSON(data):
  '''Exports scraped data to JSONs in disk.'''

  print '%s Exporting datasets JSON to disk.' % item('bullet')

  #
  # Default directory.
  #
  d = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
  data_dir = os.path.join(d, 'data')

  #
  # Calling JSON generators
  # to the default dir.
  #
  ExportDatasets(data, data_dir)
  ExportResources(data, data_dir)

  print '%s Successfully exported JSON files.\n' % item('success')


def Main(development=False):
  '''Wrapper.'''

  try:
    #
    # Either collect data or use
    # previously collected data from
    # database.
    #
    if development is False:
      data = Collect()
      pdata = Patch(data)

    else:
      cursor = scraperwiki.sqlite.execute('SELECT * FROM opennepal_content')
      pdata = []
      for record in cursor['data']:
        pdata.append(dict(zip(cursor['keys'], record)))

    #
    # Create static JSON files.
    #
    ExportJSON(data=pdata)
    scraperwiki.status('ok')


  #
  # Send notification if scraper fails.
  #
  except Exception as e:
    print '%s OpenNepal Scraper failed.' % item('error')
    scraperwiki.status('error', 'Collection failed.')
    os.system("mail -s 'OpenNepal: Scraper failed.' capelo@un.org")



if __name__ == '__main__':
  Main()
