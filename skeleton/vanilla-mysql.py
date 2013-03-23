#!/usr/bin/python
# -*- coding: utf-8 -*-
''' mysql vanilla connection
	install $ sudo apt-get install python-mysqldb


'''


import MySQLdb as mdb
import sys

con = None

DB_HOST = 'localhost'
DB_USER = 'client'
DB_PASS = 'pass'
DB_PORT = 3306
DB_NAME = 'graphapp'

try:
	# connection with db happens here
	db_handler = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
	db_cursor = db_handler.cursor()

db_cursor.execute("SELECT VERSION()")

data = db_cursor.fetchone()
   
print "Database version : %s " % data
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    if db_cursor :    
        db_handler.close()
