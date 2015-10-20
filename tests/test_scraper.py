#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'app'))

# testing
import mock
import unittest
from mock import patch

# program
import app.scrape.scrape as Scraper

class TestScraperFunctions(unittest.TestCase):
  '''Unit tests for testing if the scraper is working as expected.'''

  def test_scrape_urls_returns_array(self):
    d = Scraper.ScrapeURLs(0, verbose=True)
    assert type(d) == type([])

  def test_scrape_content_returns_dictionary(self):
    u = Scraper.ScrapeURLs(0, verbose=True)
    d = Scraper.ScrapeContent(u[0]['url'], verbose=True)
    assert type(d) == type({})
