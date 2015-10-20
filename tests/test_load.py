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
import app.utilities.load as Load

#
# Constant.
#
_split = os.path.split
CONFIG_DIR = os.path.join(_split(_split(os.path.realpath(__file__))[0])[0], 'config')

class TestUtilitiesLoad(unittest.TestCase):
  '''
  Unit tests for testing the utility for loading
  JSON configuration files works as expected.
  '''

  def test_load_config(self):
    data = os.path.join(CONFIG_DIR, 'dev.json')
    result = Load.LoadConfig(data)
    assert type(result) == type({})

    data = os.path.join(CONFIG_DIR, 'prod.json')
    result = Load.LoadConfig(data)
    assert type(result) == type({})
