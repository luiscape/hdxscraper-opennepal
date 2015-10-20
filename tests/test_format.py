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
import app.utilities.format as Format

class TestUtilitiesFormat(unittest.TestCase):
  '''
  Unit tests for testing the utility for formatting terminal output
  works as expected.
  '''

  def test_patch_item(self):
    data = 'bullet'
    result = Format.item(data)
    assert type(result) == type(u'string')

    data = 'error'
    result = Format.item(data)
    assert type(result) == type(u'string')

    data = 'warn'
    result = Format.item(data)
    assert type(result) == type(u'string')

    data = 'success'
    result = Format.item(data)
    assert type(result) == type(u'string')
