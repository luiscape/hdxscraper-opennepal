#!/usr/bin/python
# -*- coding: utf-8 -*-

import scraperwiki
import scrape.scrape as Scraper
from utilities.format import item
from utilities.db import CleanTable, StoreRecords

def Main():
  '''Wrapper.'''

  try:
    #
    # Collecting URLs from OpenNepal.
    #
    print '%s Collecting data from OpenNepal.' % item('bullet')

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

  except Exception as e:
    print '%s OpenNepal Scraper failed.' % item('error')
    scraperwiki.status('error', 'Collection failed.')
