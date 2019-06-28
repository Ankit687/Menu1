#!/usr/bin/python36
def create_hadoop():
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
		#sp.say("what you wanna do in haddop")
		#sp.runAndWait()
		print("what you wanna do in hadoop")
		#sp.say(" press 1: to create a master of ur hadoop system")
		#sp.runAndWait()
		print("press 1:  to create a master of ur hadoop system")
		#sp.say("press 2: to create a datanode of ur hadoop system")
		#sp.runAndWait()
		print("press 2: to create a datanode of ur hadoop system")
		#sp.say("press 3: to create client of your hadoop system")
		#sp.runAndwait()
		print("press 3: to create client of your hadoop system")
		#sp.say("press 4: if you want to upload some data or file in hadoop")
		#sp.runAndWait()
		print("press 4: to create master of hadoop computing cluster")
		print("press 5: to create nodes(tasktracker) of your hadoop computing cluster")
		print("press 6: to upload file in the hadoop storage cluster")		
		#sp.say("press 5: if you want to retrive your data")
		#sp.runAndWait()
		print("press 7: if you want to retrive your data")
		print("press 8: if you want to compute something using computing something")
	
		
		
		choice = int(input("enter your choice"))
		if choice == 1:
			nn =   sb.getstatusoutput("ansible-playbook hadoop_nn.yml")
			if nn[0] == 0:
				#sp.say("master created successfully")
				#sp.runAndWait()
				print("master created successfully")
			else:
				#sp.say("there is some problem please check your entry")
				#sp.runAndWait()
				print("there is some problem please check your entry")
		elif choice == 2:
			dn  = sb.getstatusoutput("ansible-playbook hadoop_nn.yml")
			if dn[0] == 0:
				#sp.say("datanodes created successfully")
				#sp.runAndWait()
				print("datanodes created successfully") 
			else:
				#sp.say("there is some problem please check your entry")
				#sp.runAndWait()
				print("there is some problem please check your entry")

		elif choice == 3:
			cn = sb.getstatusoutput("ansible-playbook client.yml")
			if cn[0] == 0:
				#sp.say("client created successfully")
				#sp.runAndWait()
				print("client created successfully")
			else:
				#sp.say("there is some problem please check your entry")
				#sp.runAndWait()
				print("there is some problem please check your entry")
		elif choice == 4:
		        cn = sb.getstatusoutput("ansible-playbook jt_nn.yml")
		        if cn[0] == 0:
		                #sp.say("client created successfully")
		                #sp.runAndWait()
		                print("client created successfully")
		        else:
		                #sp.say("there is some problem please check your entry")
		                #sp.runAndWait()
		                print("there is some problem please check your entry")
		elif choice == 5:
		        cn = sb.getstatusoutput("ansible-playbook jt_dn.yml")
		        if cn[0] == 0:
		                #sp.say("client created successfully")
		                #sp.runAndWait()
		                print("client created successfully")
		        else:
		                #sp.say("there is some problem please check your entry")
		                #sp.runAndWait()
		                print("there is some problem please check your entry")


		elif choice == 6:
			put  = sb.getstatusoutput("ansible-playbook hadoop_put.yml")
			if put[0] == 0:
				#sp.say("file put successfully")
				#sp.runAndWait()
				print("file put successsfully")
			else:
				#sp.say("there is some problem please check your entry")
				#sp.runAndWait()
				print("there is some problem please check your entry")
		if choice == 7:
			read = sb.getstatusoutput("ansible-playbook hadoop_read.yml")
			if read[0] == 0:
				#sp.say("please read your file")
				#sp.runAndWait(0)
				print("please read your file")
			else:
				#sp.say("there is some problem please check your entry")
				#sp.runAndWait()
				print("there is some problem please check your entry")
		else:
			#sp.say("THank you for using our tool")
			#sp.runAndWait()
			print("thank you for using our tool")
create_hadoop()
