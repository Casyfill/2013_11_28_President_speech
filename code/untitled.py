#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import re

s=u"Привет Мир!!! привет привет миррр ";
print s

hello_pattern = re.compile( u'([А-Яа-я]+)', re.UNICODE )

r = hello_pattern.findall( s )

for l in r:
	print l