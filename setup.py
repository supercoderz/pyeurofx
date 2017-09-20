#!/usr/bin/env python

from distutils.core import setup

setup(name='pyeurofx',
	  version='0.6.4',
	  description='Python module to get and parse daily and historical FX rates from ECB',
	  long_description='Please visit https://github.com/supercoderz/pyeurofx for more details',
	  author='Narahari Allamraju',
	  author_email='anarahari@gmail.com',
	  url='https://github.com/supercoderz/pyeurofx',
	  packages=['eurofx'],
	  install_requires=['lxml','requests','pandas'],
	classifiers = [
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3',
	]
	 )
