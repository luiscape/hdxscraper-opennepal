#!/usr/bin/python
# -*- coding: utf-8 -*-

from termcolor import colored as color

def item(i):
  dictionary = {
    'bullet': color(u" →", "blue", attrs=['bold']),
    'error':  color(u" ERROR:", "red", attrs=['bold']),
    'success': color(u" SUCCESS:", "green", attrs=['bold']),
    'warn': color(u" WARN:", "yellow", attrs=['bold'])
  }

  return dictionary[i]
