#!/usr/bin/python36

print("content-type: text/html")
print()

cmd = "sudo docker stop myos1"
import subprocess as sb
output = sb.getoutput(cmd)
print(output)
