#!/usr/bin/python36
import cgi
print("content-type: text/html")
print()

data = cgi.FieldStorage()

import subprocess as sb
username = data.getvalue('user')
passwd = data.getvalue('passwd')
email_id = data.getvalue('receiver')
subject = data.getvalue('subject')
body = data.getvalue('message')
body = "'{}'".format(body)
subject = "'{}'".format(subject)
choice = data.getvalue('yesno')
if(choice == 'on'):
	send_mail = 'sudo ansible-playbook --vault-password-file=secret  email.yml --extra-vars "email={} subject={} body={}" --connection local'.format(email_id,subject,body)
else:
	send_mail = 'sudo ansible-playbook email1.yml --extra-vars "user_name={} gmail_pass={} email={} subject={} body={}" --connection local'.format(username,passwd,email_id,subject,body)
if(sb.getstatusoutput(send_mail)):
		print("<h1>Mail is sent")
else:
		print("<h1>Error")
	

