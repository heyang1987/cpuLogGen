import sys
import datetime
import time
import socket
import struct
import random
 
fName = sys.argv[1]
f = open(fName, "w+")

ip_to_number = lambda ip: struct.unpack('!I', socket.inet_aton(ip))[0]
number_to_ip = lambda num: socket.inet_ntoa(struct.pack('!I', num))  
t_stamp = int(time.mktime(datetime.datetime.strptime("2014-10-31 00:00", "%Y-%m-%d %H:%M").timetuple()))

mystr = '\n'.join([ str(t)+'\t'+number_to_ip(ip)+'\t'+str(cpu_id)+'\t'+str(random.randint(0,100)) for t in range(t_stamp,t_stamp+60*60*24,60) for ip in range(ip_to_number("192.168.0.10"), ip_to_number("192.168.3.242")) for cpu_id in range(2) ])
f.write("timestamp\tIP\tcpu_id\tusage\n"+mystr)
f.close()