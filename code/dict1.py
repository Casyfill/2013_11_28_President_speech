#-*- coding: utf-8 -*-
# import sys
import os
from nltk.stem import SnowballStemmer
import re
stemmer = SnowballStemmer("russian")

filename = '/Users/andy/Dropbox/Projects/Kats/RIA/2013_11_28_President_speech/texts/2000_pu.txt'
import chardet
import codecs


# Класс словаря



# РАСПОЗНАЕМ КОДИРОВКУ
bytes = min(32, os.path.getsize(filename))
raw = open(filename, 'rb').read(bytes)

if raw.startswith(codecs.BOM_UTF8):
    encoding = 'utf-8-sig'
else:
    result = chardet.detect(raw)
    encoding = result['encoding']

infile = codecs.open(filename, 'r', encoding=encoding)
txt = infile.read()
infile.close()

# ПЕРЕВОДИМ В ЮНИКОД
text = unicode(txt)


#СОСТАВЛЯЕМ СЛОВАРЬ РЕГУЛЯРОЧКОЙ
hello_pattern = re.compile( u'([А-Яа-я]+)', re.UNICODE )
Wlist = hello_pattern.findall( text )

# ПЕЧАТАЕМ
# for l in Wlist:
# 	word = unicode(l).lower()
# 	print word,'|',stemmer.stem(word)

# СТЕММИМ И СОСТАВЛЯЕМ СЛОВАРИК
Text_Dict = {}

for w in Wlist:
	word = unicode(w).lower()
	wStemmed = stemmer.stem(word)
	if wStemmed not in Text_Dict.keys():
		Text_Dict[wStemmed]={}
		Text_Dict[wStemmed]['dict'] = []
		Text_Dict[wStemmed]['dict'].append(word)
		Text_Dict[wStemmed]['count'] = 1
	else:
		Text_Dict[wStemmed]['dict'].append(word)
		Text_Dict[wStemmed]['count'] += 1


# РАЧИТЫВАЕМ И ПЕЧАТАЕМ СТАТИСТИУ

resList = []
for key in Text_Dict.keys():
	# print key , ':', (', ').join(Text_Dict[key])
	rString =  key + '|' + str(Text_Dict[key]['count'])  + '|' + (',').join(Text_Dict[key]['dict'])
	print rString
	rString+='\n'
	resList.append(rString.encode('utf-8'))

resList[-1].replace('\n','')
# print resList

workfile ='/Users/andy/Dropbox/Projects/Kats/RIA/2013_11_27_Speeches/Dicts/2000_pu.csv'
with open('workfile', 'w') as f:
	write_data = f.writelines(resList)
f.closed
print 'done'


