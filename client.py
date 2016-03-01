import socket
import psutil, time
udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # membuat udp soket
toaddress = ('192.168.1.3', 55555)  # socket address for 192.168.0.11 using port 55555

while 1:
    memory=psutil.virtual_memory()[2]
    #kirim=time.strftime('%d-%m-%Y %H:%M:%S',time.localtime()),'CPU= ','%' ,'memory=',memory
    ins="%"
    h=round(psutil.cpu_percent(),1)
    tgl=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    cpu="%g"%h
    s="(%s) CPU = %s%s ,\t Memory = %s%s"%(tgl,h,ins,memory,ins)
    print s
    udpsock.sendto(s, toaddress)  # send message
    time.sleep(5)


udpsock.close()  # close the socket