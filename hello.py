#!/usr/bin/python36

import cgi
import subprocess as sb


mydata = cgi.FieldStorage()
value  = mydata.getvalue('q')
value2 = mydata.getvalue('p')

print("content-type: text/html")
print()
print("What up. Python here")
print("\n", value)
print(value2)
