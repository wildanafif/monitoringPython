#!/usr/bin/env python

"""
buatlah sebuah program untuk menerima paket unicast UDP
yang masuk dari seluruh interface pada port 55555
"""

import socket  # referensi: https://docs.python.org/2/library/socket.html

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create udp sock
sockaddress = ('', 55555)  # socket address for all interface using port 55555
udpsock.bind(sockaddress)  # bind the socket



while 1:
	data, fromaddr = udpsock.recvfrom(2048)  # wait for message
	print fromaddr[0], data

udpsock.close()  # close the socket
