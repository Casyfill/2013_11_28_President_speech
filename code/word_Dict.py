#-*- coding: utf-8 -*-
""" Обрабатывает файл и создает частотный словарь (частота повторения слова в тексте) """
 
import sys
import os
import re
 

 
work_file = '/Users/andy/Dropbox/Projects/Kats/2013_11_28_President_speech/texts/2000_pu.txt'
# if os.path.isfile(work_file):
#     print('Рабочий файл: ' + work_file) 
# # читаем файл

file = open(work_file,'r', )
try:
    txt = file.read()
    txt.decode('utf-8', 'ignore')
finally:
    file.close()

# print txt
# txt = 'Семен наварил щей, - сообщил почтальон'
# txt.decode('ascii', 'ignore').lower()
# # print len(txt)
 
# выбираем слова через регулярные выражения
# p = re.compile(u"[\u0400-\u0500]+")
# res=p.findall(txt)

d = re.findall('([А-Яа-я]+)',txt) 

# print len(res)
# print 'match done'
# print res

for w in d:
	w.decode('utf-8', 'ignore')
	print w

print 'Але=Хоп!'