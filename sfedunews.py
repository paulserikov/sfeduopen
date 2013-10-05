# -*- coding: utf-8 -*-

# last news id 45341
# 404 page may not be as 404 apache page
# http://sfedu.ru/www/sfedu$news$.show_full?p_nws_id=43952
# working page

# redir http://sfedu.ru/404.shtml
# errors: 4014 (en)

import time
import urllib
from BeautifulSoup import BeautifulSoup

ce = 0
cs = 0

start_time = time.time()

f = open('sfedupostnames.txt', 'w')

for i in range (4015,46000):
	page = urllib.urlopen("http://sfedu.ru/www/sfedu$news$.show_full?p_nws_id="+str(i))
	soup = BeautifulSoup(page.read(), fromEncoding="win-1251")
	print i

	if soup.find('h1'):
		if soup.find('h1').string == "Ошибка 404".decode('utf-8'):
			print "Страницы с id = "+str(i)+" не существует"
			ce +=1
		else:
			A = soup.find('div', attrs={'class': 'content_top'}).h1.string
			B = soup.find('div', attrs={'class': 'content_bottom_date'}).string 
			print A
			print B
			f.write(str(i)+'\t'+str(B)+'\t'+str(A)+'\n')
			cs +=1	
	else:
		print "Maybe English version"
git c

Total = time.time() - start_time, "seconds"
print Total

f.write('\n\n'+str(Total)+'\n')
f.write('Good url: '+str(cs)+'\n')
f.write('Bad url: '+str(ce)+'\n')

f.close()

print Total
print "Кaчественных:"+str(cs)
print "Некaчественных:"+str(ce)
