#!/usr/bin/python
# -*- coding: utf-8 -*-

import urlparse
import requests
from bs4 import BeautifulSoup

def ScrapeURLs(page, filters=True, verbose=False):
  '''Scrapes the OpenNepal website for dataset URLs.'''

  if verbose:
    print 'Scraping the OpenNepal page: %s' % page

  #
  # Assemble URL.
  #
  u = 'http://data.opennepal.net/datasets?page=%s' % page
  if filters is True:
    u += 'field_dataset_sector_tid[0]=107&field_dataset_sector_tid[1]=7&field_dataset_sector_tid[2]=112&field_dataset_sector_tid[3]=146&field_dataset_sector_tid[4]=144&field_dataset_sector_tid[5]=147&field_dataset_sector_tid[6]=148&field_dataset_sector_tid[7]=100&field_dataset_sector_tid[8]=183&field_dataset_sector_tid[9]=217'


  try:

    #
    # Download data from OpenNepal's website.
    #
    r = requests.get(u)

    #
    # Find data with BeautifulSoup.
    #
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.findAll('table')

    keys = ['url']
    out = []
    i = 0
    for row in table[0].findAll('tr'):
      if i == 0:
        i += 1
        continue

      else:
        #
        # Finds href.
        #
        url = [ 'http://data.opennepal.net' + row.findAll('a', href=True)[0]['href'] ]

        out.append(dict(zip(keys, url)))
        i += 1

    return out


  except Exception as e:
    print 'Failed to scrape data from OpenNepal website'
    print e
    return False


def ScrapeContent(url, verbose=False):
  '''Scraping content from each dataset.'''

  if verbose:
    print 'Scraping the OpenNepal dataset: %s' % url

  #
  # Download data from OpenNepal's website.
  #
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')

  #
  # Title.
  #
  title = soup.select('#page-title')[0].text

  #
  # Tags.
  #
  tags = []
  region = soup.select('.region-inside')
  for tag in region[0].select('.field-item'):
    tags.append(tag.text)

  #
  # License and date.
  #
  license = soup.select('.ds-mid-right')[0].select('.field-item .even')[0].text.replace('\n', '')
  date = soup.select('.ds-mid-right')[0].select('.date-display-single')[0].text.rstrip()

  #
  # Description.
  #
  description = soup.select('.field-type-text-with-summary')[0].select('.field-item')[0].text

  #
  # Resource name, link, and type.
  #
  resource = {
    'url': 'http://data.opennepal.net',
    'name': None,
    'type': None
  }
  resource['url'] += soup.select('.view-resource-download')[0].findAll('a', href=True)[0]['href']
  resource['name'] = resource['url'].split('/')[-1].split('&')[0]
  resource['type'] = resource['name'].split('.')[1].upper()

  out = {
    'title': title,
    'license': license,
    'tags': tags[0].replace('/', '-'),
    'date': date,
    'description': description,
    'resource_url': resource['url'],
    'resource_name': resource['name'],
    'resource_type': resource['type']
  }

  return out
