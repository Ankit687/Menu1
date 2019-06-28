#!/usr/bin/python36
print("content-type: text/html")
print()

import cgi

print("""
<form action=http://192.168.43.190/cgi-bin/shellinabox.py>
<table>
<tr>
<td>
<b> enter your ip   </b>
</td>
<td>
<input type=text name=id>  
</td>
</tr>
</table>
<input type=submit name=choice >
</form>
""")
data=cgi.FieldStorage()
ip = data.getvalue("id")
choice = data.getvalue("choice")

if ip is None and "Submit" in choice :
	print("Enter ip first")
elif 'Submit' in choice:
	print("""
	<a href=http://{}:4200 target=google > my shell  </a>

<iframe name=google width=400px height=400px>  </iframe>

""".format(ip))
