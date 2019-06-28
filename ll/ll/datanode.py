#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi
import subprocess as sp

data = cgi.FieldStorage()
master_ip = data.getvalue("master_ip")
folder = data.getvalue("folder")
cmd = "sudo ansible-playbook ./playbooks/hadoop_dn.yml --extra-vars 'master_ip={} folder={}' --connection local".format(master_ip,folder)
print(sp.getoutput(cmd))
if sp.getstatusoutput(cmd) == 0:
	print("<h1>Data node created")
else:
	print("<h1>Something get error")
