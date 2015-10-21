#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
from copy import copy
from datetime import datetime

def ExportDatasets(data, directory=None):
  '''Function to export datasets in a JSON format.'''

  if directory == None:
    print 'Provide directory.'

  #
  # Default dataset.
  #
  default_dataset = {
    'name': None,
    'title': None,
    'owner_org': 'opennepal',  # default for OpenNepal
    'author': '',
    'author_email': '',  # default for OpenNepal
    'maintainer': '',  # default for OpenNepal
    'maintainer_email': '',  # default for OpenNepal
    'license_id': 'hdx-other',  # default for OpenNepal
    'license_other': None,
    'dataset_date': None,  # has to be in MM/DD/YYYY format.
    'subnational': 0,  # has to be 0 or 1. Default 1 for OpenNepal.
    'notes': None,
    'caveats': None,
    'methodology': 'Other',  # default for OpenNepal
    'methodology_other': None,
    'dataset_source': 'OpenNepal',
    'package_creator': 'luiscape',
    'private': False,  # has to be True or False
    'url': None,
    'state': 'active',  # always "active"
    'tags': [],  # has to be a list with {'name': None}
    'groups': []  # has to be ISO-3-letter-code. {'id': None}
    }

  out = []
  for record in data:

    t = default_dataset

    #
    # Adding fields from records.
    #
    t['name'] = record['id']
    t['title'] = 'Nepal - ' + record['title']  # patching names.
    t['notes'] = record['description']
    t['dataset_date'] = record['dataset_date']

    #
    # Adding license.
    #
    license = record.get('license', None)
    if license is not None:
      t['license_other'] = license
      if license == 'Open Data Commons Open Database License (ODbL)':
        t['license_id'] = 'hdx-odc-odbl'

    #
    # Adding tags and country.
    #
    t['tags'] = [{ 'name': record['tags'] }]
    t['groups'] = [{ 'id': 'npl' }]


    #
    # Appending results.
    #
    out.append(copy(t))

  #
  # Write JSON to disk.
  #
  with open(os.path.join(directory, 'datasets.json'), 'w') as outfile:
    json.dump(out, outfile)



def ExportResources(data, directory=None):
  '''Export the UNOSAT resources for their respective datasets.'''

  #
  # Default resource.
  #
  default_resource = {
    "package_id": None,
    "url": None,
    "name": None,
    "format": None,
    "description": None  # file size could go here.
  }

  out = []
  for record in data:

    t = default_resource

    #
    # Adding fields from records.
    #
    t['package_id'] = record['id']
    t['url'] = record['resource_url']
    t['name'] = record['resource_name']
    t['format'] = record['resource_type']

    #
    # Appending results.
    #
    out.append(copy(t))

  #
  # Write JSON to disk.
  #
  with open(os.path.join(directory, 'resources.json'), 'w') as outfile:
    json.dump(out, outfile)
