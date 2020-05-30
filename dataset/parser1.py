import re
import csv
import json
import uuid
import time
import json
import random
import hashlib
import requests

from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

for i in range(1, 376):
	print(i)
	link = r'http://government.ru/docs/?page=' + str(i)
	page = get_html(link)
	soup = BeautifulSoup(page, 'lxml')
	links = soup.find_all('a', class_='headline__link open-reader-js')
	time.sleep(30)
	for link in links:		
		a = link.get('href')
		n = a.split('/')[2]
		l = 'http://government.ru' + a
		p = get_html(l)
		sp = BeautifulSoup(p, 'lxml')
		try:
			title = sp.find('h3', class_='reader_article_headline').text
			pdf_url = sp.find('a', class_='entry_file_link').get('href')
			pdf = requests.get(pdf_url)
			dc = {'number': n.strip(), 'title': title.strip()}
			with open(r'pdf/' + 'title.csv', 'a') as f:
				[f.write('{0}\t'.format(value)) for key, value in dc.items()]
				f.write('\n')
			
			with open(r'pdf/' + n + '.pdf', 'wb') as f:
				f.write(pdf.content)
		except (AttributeError, UnicodeDecodeError, UnicodeEncodeError) as e:
			continue