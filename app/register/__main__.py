#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import scraperwiki

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.load import LoadConfig
from termcolor import colored as color
from utilities.format import item as I
from register import load, delete, create


def Main():
  '''Wrapper'''

  #
  # Setting up configuration: dev = development; prod = production.
  #
  p = LoadConfig(os.path.join(os.path.split(dir)[0], 'config', 'prod.json'))
  if p is not False:

    print "--------------------------------------------------"
    print '%s HDX Site: %s' % (I('bullet'), p['hdx_site'])

    #
    # Deleting all datasets from org.
    #
    if p['delete_datasets']:
      try:
        delete.DeleteAllDatasetsFromOrg(organization='opennepal', hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'])

      except Exception as e:
        print e
        return False

    try:
      #
      # Loading JSON data.
      #
      dataset_dict = load.LoadData(os.path.join(p['json_folder'], 'datasets.json'))
      resource_dict = load.LoadData(os.path.join(p['json_folder'], 'resources.json'))
      # gallery_dict = load.LoadData(os.path.join(p['json_folder'], 'gallery.json'))

      # Delete resources before running:
      if p['delete_resources']:
        delete.DeleteResources(dataset_dict=dataset_dict, hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'])

      if p['update_all_datasets']:
        print '--------------------------------------------------'
        print color(u" ATTENTION:", "blue", attrs=['bold']) + ' Updating ALL datasets.'
        print '--------------------------------------------------'

      #
      # Create datasets, resources, and gallery items.
      #
      create.CreateDatasets(dataset_dict=dataset_dict, hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])
      create.CreateResources(resource_dict=resource_dict, hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])
      # create.CreateGalleryItems(gallery_dict=gallery_dict, hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])

    except Exception as e:
      print e
      return False



if __name__ == '__main__':

  if Main() != False:
    print '%s OpenNepal scraper registered datasets successfully.\n' % I('success')
    scraperwiki.status('ok')

  else:
    scraperwiki.status('error', 'Failed to register resources.')
    os.system("mail -s 'OpenNepal scraper failed to register datasets' luiscape@gmail.com")
