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
	
def get_data(html):	
	soup = BeautifulSoup(html, 'lxml')	
	cells = soup.find_all('div', class_='b26-tableItem')
	for cell in cells:
		time.sleep(10)
		url = r'http://archive.government.ru' + cell.find('h3').find('a').get('href')		
		desc = cell.find('p', class_='description').text
		h = get_html(url)
		sp = BeautifulSoup(h, 'lxml')
		text = sp.find('div', class_='text-main')
		text = text.find_all('p')
		s1 = 'Председатель ПравительстваРоссийской Федерации Д.Медведев'
		s2 = 'Председатель Правительства Российской Федерации Д.Медведев'
		s3 = 'Председатель ПравительстваРоссийской Федерации В.Путин'
		s4 = 'Председатель Правительства Российской Федерации В.Путин'
		txt = ''
		for t in text:
			txt += t.text.replace(s1, '').replace(s2, '').replace(s3, '').replace(s4, '').replace('\n', ' ')
		with open('dataset2.csv', 'a', encoding='utf-8', newline='') as csv_file:
			writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
			writer.writerow([desc,txt])
			
def main(i):
    url = r'http://archive.government.ru/gov/results/?page='+str(i)
    return get_data(get_html(url))
	
if __name__ == '__main__':
	for i in range(1, 400):
		print(i)
		main(i)






'''
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
'''