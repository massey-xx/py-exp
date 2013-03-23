#!/usr/bin/python

import sys
from os.path import basename
from syslog import closelog, openlog, syslog, LOG_INFO, LOG_ERR, LOG_USER
'''
infile = open('site.txt', 'r')

#print infile

for line in infile:
	print line,
'''
def main():
	'''
	 vanilla main template that include logging
	'''
	openlog(basename(sys.argv[0]), 0, LOG_USER)
	try:
		print "Something"
		
		invoke = ''
		for arg in sys.argv:
			invoke = invoke + "+" + arg
		syslog(LOG_USER, u'invoked as: %s ' % invoke) 
		 
	except Exception, e:
		syslog(LOG_ERR, u'An error occurred: %s' % unicode(e))
	finally:
		closelog()


if __name__ == '__main__':
	main()
