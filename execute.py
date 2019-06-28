#!/usr/bin/python36
print("content-type: text/html")
print()

i=1
def service_management(service, state, host):
    cmd = "sudo ansible-playbook service.yml --extra-vars='host={} service_name={} states={}' --connection local".format(host, service, state)
    output = sb.getoutput(cmd)
    print(output)
    return output

def get_cur_location():
    response_data = requests.get('https://ipinfo.io/').text
    print(response_data)
    try:
        response_json_data = json.loads(response_data)
        location = response_json_data["loc"].split(",")
        print("Latitude: %s" % location[0])
        print("Longitude: %s" % location[1])
        return location
    except ValueError:
        print("Exception happened while loading data")

def get_directions():
    coord = get_cur_location()
    lat, lang = coord[0], coord[1]
    end = "LinuxWorld Informatics Pvt. Ltd., Plot No. 5, Krishna Tower Next to Triveni Nagar Flyover, Gopal Nagar-A, Agrasen Nagar, Gopal Pura Mode, Gopalpura, Jaipur, Rajasthan 302015".replace(" ", "+")
    url = "https://www.google.com/maps/dir/"+lat+","+lang+"/"+end
    print("""
        <a href={} target=_blank name=maps>Click to view direction</a>
    """.format(url))
    return url


def hadoop():
    print("<a href=http://192.168.43.190/cgi-bin/playbooks/hadoop.py name='email'>Click here for hadoop</a>")

def shellinthebox():
    output = sb.getoutput('sudo setenforce 0')
    print(output)
    output = sb.getoutput('sudo systemctl start shellinaboxd')    
    print(output)
    output = sb.getoutput('sudo systemctl stop firewalld')
    print(output)
    
def firefox():
    i = 1
    cmd = "docker run -itd -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --name new{} firefox_final:v2".format(i)
    output = sb.getoutput(cmd)
    print(output)
    cmd = "docker inspect "+ output+" | grep IPAddress"
    output2 = sb.getoutput(cmd)
    ipaddr = output2.split("\n")
    ipaddr = ipaddr[1].split(":")[1].replace('"','').replace("'","").replace(",","").replace(" ","")
    cmd = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null {} -X firefox".format(ipaddr)
    output3 = sb.getoutput(cmd)
    i += 1
    
def firefox_stop(i):
    sb.getoutput("docker stop new{}".format(i))

import cgi, subprocess as sb, requests, json
values = cgi.FieldStorage()
command = values.getvalue("command")
if command == None:
     choice = ' '
else:
     choice = command.lower()
print(command)
if 'service' in choice and ('start' in choice or 'stop' in choice):
        print(choice)
        #if "http" in choice:
            #service = "httpd"
        #elif "ftp" in choice:
            #service = "vsftpd"
        #if 'start' in choice:
            #state = 'started'
        #elif 'stop' in choice:
            #state = 'stopped'
        #if 'local' in choice:
            #host = 'local'
        #elif 'remote' in choice:
            #host = 'remote'
        service = "httpd"
        state = "started"
        host = "local"	
        print(service, state, host)
        output = service_management(service,  state, host)
        print(output)
        print("<h1>{} {}</h1>".format(service, state))

elif 'location' in choice:
    location = get_cur_location()
    print(location)

elif 'direction' in choice:
    url = get_directions()
    
elif 'send mail' in choice:
    print("<a href=http://192.168.43.190/email.html name='email'>Click here for mail</a>")

elif 'hadoop cluster' in choice:
    print("<a href=http://192.168.43.190/hadoop.html name='hadoop'>Click here for hadoop cluster configurations</a>")

elif 'shell in a box' in choice:
    shellinthebox()
    print("<a href=shellinabox.py name=shell>Click here to open the shell</a>")
    
elif 'docker management' in choice:
    print("<a href=main_docker.py name'docker' Click here to open docker management</a>")
    
elif 'launch firefox' in choice:
    firefox()
    
elif 'elastic container' in choice:
    output = sb.getoutput("sudo ansible-playbook --vault-password-file=secret ./ec2.yml --connection local")
    print(output)

elif 'storage' in choice:
    output = sb.getoutput("sudo ansible-playbook --vault-password-file=secret ./s3.yml --extra-vars='bucket_name=4k2' --connection local")
    print(output)
elif 'disk partition' in choice:
    print("<a href=http://192.168.43.190/cgi-bin/disk-partition.py name='disk'>Click here for partitioning</a>")

elif 'lvm create' in choice:
    print("<a href=http://192.168.43.190/cgi-bin/lvm-partition.py name='lvm'>Click here for creating logical volume</a>")
# elif 'docker launch' in choice:
#     sb.subprocess('./docker.py')

#print('<button><a href="file:///H:/menu/voice.html">Go back</a></button>')
