#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sb

cmd = "sudo docker images | grep v3"

output = sb.getoutput(cmd)
images = output.split('\n')
print(
    """
    <table border='5'>
    <th>
    </th>
    """)
print(images)
for i in images[1:]:
    j = i.split()
    print(j)
    print(
    """<tr>
       <td>{}</td>
       <td>{}</td>
       <td>{}</td>
       <td>{}</td>
    </tr>""".format(j[0], j[1], j[2], j[3]))
print("""
    </table>
    """)


