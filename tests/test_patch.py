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
import app.scrape.patch as Patch

class TestPatchUnits(unittest.TestCase):
  '''Unit tests for testing the patching works as expected.'''

  def test_patch_date(self):
    data = 'August 13, 2015'
    result = Patch.Date(data)
    assert type(result) == type('string')

  def test_patch_slug(self):
    data = 'Dataset With Rather Large Name'
    result = Patch.Slug(data)
    assert type(result) == type('string')

  def test_length_slugh(self):
    data = 'At Times, The Horizon Reaches Unreachable Ends' + \
           'Those Ends Find Horizons Withing Their Own Colors' + \
           'Which Defy What We Understand as the Horizons of Colors'
    result = Patch.Slug(data)
    assert len(result) == 90
