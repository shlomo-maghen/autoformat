import os
from bs4 import BeautifulSoup as bs
import sys

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')

	if len(sys.argv) == 2:
		sites_folder = sys.argv[1]
	else:
		sites_folder = 'sites'
	files = os.listdir(sites_folder)
	folders = [f for f in files if os.path.join(sites_folder, f)]
	print 'processing folders ' + ', '.join(folders)
	not_code_file = open(os.path.join('samples', 'not_code.txt'), 'w+')

	for folder in folders:
		label = folder
		code_file = open(os.path.join('samples', label + '.txt'), 'w+')
		code_folder = os.path.join(sites_folder, folder)
		sites = os.listdir(code_folder)
		for site in sites:
			print 'processing file {}'.format(site)
			with open(os.path.join(code_folder, site)) as site:
				soup = bs(site, 'html.parser')
				codes = soup.find_all('code', text=True)
				for code in codes:
					for line in code:
						code_file.write(line.string + '\n')
				not_codes = soup.find_all('p', text=True)
				for not_code in not_codes:
					for line in not_code:
						not_code_file.write(line.string + '\n')
		code_file.close()
	not_code_file.close()

	print 'done'



if __name__ == '__main__':

	main()