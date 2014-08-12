#!/usr/bin/python

import sys, getopt, subprocess
import urllib

def html2rst(html):
	p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	return p.communicate(html)[0]

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hu:o:",["url=","file="])
	except getopt.GetoptError:
		print 'test.py -u url -f file'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -u <input url> -f <input file>'
			sys.exit()
		elif opt in ("-u", "--url"):
			url = arg
			print('Opening url {0}'.format(url))
			try:
				f = urllib.urlopen(url)
				print(html2rst(f.read()))
				f.close()
			except:
				print('Invalid URL')
				sys.exit(2)

		elif opt in ("-f", "--file"):
			file = arg
			print('Opening file {1}'.format(file))


if __name__ == "__main__":
	main(sys.argv[1:])
