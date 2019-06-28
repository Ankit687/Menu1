#!/usr/bin/python36

print("content-type: text/html")
print()


import subprocess as sb
import cgi

values = cgi.FieldStorage()
print(values.getvalue("docker_name"))
print(values.getvalue("docker_image"))



docker_name = values.getvalue("docker_name")
docker_image = values.getvalue("docker_image")
#print(docker_name)
print()
#print(docker_image) 
print()


print("Hello World!")
print()
print()
output = sb.getoutput("sudo docker run -itd --name " + docker_name + " " + docker_image)
print(output)
