#!/usr/bin/env python

from distutils.core import setup

setup(name='pyeurofx',
      version='0.1',
      description='Python module to get and parse daily and historical FX rates from ECB',
      long_description='Please visit https://github.com/supercoderz/pyeurofx for more details',
      author='Narahari Allamraju',
      author_email='anarahari@gmail.com',
      url='https://github.com/supercoderz/pyeurofx',
      packages=['eurofx'],
      requires=['lxml','requests','pandas'],
     )
