#!/usr/bin/python36

print("content-type: text/html")
print()


import subprocess as sb
output = sb.getoutput("ssh -X root@192.168.43.190 -p 80:22 cheese")
#output = sb.getoutput("cheese")
print(output)

