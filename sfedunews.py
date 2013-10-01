# -*- coding: utf-8 -*-

# last news id 45341
# 404 page may not be as 404 apache page
# http://sfedu.ru/www/sfedu$news$.show_full?p_nws_id=43952
# redir http://sfedu.ru/404.shtml

import time
import urllib
from BeautifulSoup import BeautifulSoup

ce = 0
cs = 0

start_time = time.time()

f = open('sfedupostnames.txt', 'w')

for i in range (0,46000):
	page = urllib.urlopen("http://sfedu.ru/www/sfedu$news$.show_full?p_nws_id="+str(i))
	soup = BeautifulSoup(page.read(), fromEncoding="win-1251")
	if soup.find('h1').string == "Ошибка 404".decode('utf-8'):
		print "Страницы с id = "+str(i)+" не существует"
		ce +=1 		
	else:
		cs +=1
		A = soup.find('div', attrs={'class': 'content_top'}).h1.string
		B = soup.find('div', attrs={'class': 'content_bottom_date'}).string
		print i
		print A
		print B
		f.write(str(i)+'\t'+str(B)+'\t'+str(A)+'\n')

Total = time.time() - start_time, "seconds"
print Total

f.write('\n\n'+str(Total)+'\n')
f.write('Good url: '+str(cs)+'\n')
f.write('Bad url: '+str(ce)+'\n')

f.close()

print Total
print "Кaчественных:"+str(cs)
print "Некaчественных:"+str(ce)
