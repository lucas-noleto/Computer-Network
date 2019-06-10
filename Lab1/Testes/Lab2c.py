import socket
import requests

# for  p in range(10000):
# 	tcp = socket.getservbyport(p)
# 	print(p,tcp)	
 	

# tcp = socket.getservbyport(1,)
# print(1,tcp)	
# 	# if tcp is not None:	
	
# 	# if udp is not None:
for  p in range(10000):
	
	tcp = socket.getservbyport(p,)
	print(p,tcp)	
