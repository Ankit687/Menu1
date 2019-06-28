#!/usr/bin/python36
import subprocess as sb
import getpass
import cgi
import signal

print("content-type: text/html")

print()

password = "redhat"
print("enter passwd")
menu_pass = getpass.getpass("enter password")
#print("enter password")


def interupt(x,y):
	print(" \n thank you for using my tool")
	exit()
signal.signal(2, interupt )

 
if password != menu_pass:
	print("please enter a valid password")
else:
	choice = int(input("enter your choice"))
	if choice == 0:
		count = int(input("Enter number of launch: "))
		output = sb.getstatusoutput('ansible-playbook --vault-password-file=secret ./ec2.yml --extra-vars "how_many=' + str(count) +  '"')
		if output == 0:
			print("ec2 launch successfully")
		else:
			print("there is some problem please check your connectivity")
	else:
		print("thank you for using our tool")
