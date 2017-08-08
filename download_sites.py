import sys
import re
import urllib2 as ul
import os

# update to write language specific
def main():
	print 'downloading sites'
	
	url_files = [x for x in os.listdir('.') if x[0:5] == "urls_"]
	for url_file in url_files:
		label = url_file.split("urls_")[-1][0:-4]
		with open(url_file) as f:
			urls = f.read().split('\n')
		for url in urls:
			site = ul.urlopen(url)
			file_name = '{}.txt'.format(url).replace('https://stackoverflow.com/questions/', '')
			file_name = file_name.replace(':', '-').replace('/', '-')
			print 'processing url {}'.format(url)
			with open('sites/{}/{}'.format(label, file_name), 'w+') as f:
				f.write(site.read())
	print 'done'


if __name__ == '__main__':
	main()

