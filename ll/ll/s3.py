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
           if choice == 12:
                bucket_name = input("Enter name of bucket: ")
                output = sb.getstatusoutput('ansible-playbook --vault-password-file=secret ./final_playbooks/s3.yml --extra-vars "bucket_name =' + bucket_name +  '"')
                  if output[0] == 0:
		     sp.say("bucket created and configured automatically")
		     sp.runAndWait()
		     print("bucket created and configured autommatically")
		  else:
		     sp.say("there is some problem please check your connectivity")
		     sp.runAndWait()
                     print("there is some problem please check your connectivity")
	   else:
		#sp.say("THank you for using our tool")
		#sp.runAndWait()
			print("thank you for using our tool")
