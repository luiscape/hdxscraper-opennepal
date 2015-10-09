#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import scraperwiki
from scrape.patch import Slug
import scrape.scrape as Scraper
from utilities.format import item
from utilities.db import CleanTable, StoreRecords

def CollectAndStore():
  '''Scrapes and stores data in database.'''

  try:
    #
    # Collecting URLs from OpenNepal.
    #
    print '%s Collecting dataset URLs from OpenNepal.' % item('bullet')

    urls = []
    for page in range(0, 11):
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

    print '%s Collected data from OpenNepal successfully.' % item('success')
    scraperwiki.status('ok')

    return content

  except Exception as e:
    print '%s OpenNepal Scraper failed.' % item('error')
    scraperwiki.status('error', 'Collection failed.')


def Patch(data):
  '''Patching data.'''
  print '%s Patching data.' % item('bullet')

  out = []
  for record in data:
    record['id'] = Slug(record['title'])
    out.append(record)

  return out


def ExportJSON(data):
  '''Exports scraped data to JSONs in disk.'''
  #
  # Default directory.
  #
  data_dir = os.path.join(os.path.split(dir)[0], 'data')

  #
  # Calling JSON generators
  # to the default dir.
  #
  print '%s Exporting datasets JSON to disk.' % item('bullet')
  ExportDatasets(data, data_dir)
  # ExportResources(data, data_dir)

  print '%s Successfully exported JSON files.\n' % item('success')


def Main():
  '''Wrapper.'''

  data = CollectAndStore()
  data = Patch(data)
  ExportJSON(data=data)
