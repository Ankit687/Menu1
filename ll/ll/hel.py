#!/usr/bin/python36
print("content-type: text/html")
print()
import subprocess as sb


print("Adding user")
print(sb.getoutput("/usr/bin/whoami"))
output = sb.getoutput("rpm -q httpd")
print(output)
