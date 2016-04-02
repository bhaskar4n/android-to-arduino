import socket
import bluetooth
import serial
import sys
from thread import*
host = '192.168.43.96' #YOUR MACHINE IP ADDRESS
port = 12364
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ser = serial.Serial('COM3',9600) #SERIAL CONNECTION

print 'socket created'
try:
        s.bind((host,port))
except socket.error, msg:
        print 'bind failed'
        sys.exit()
print 'socket bind complete'
s.listen(10)
print 'socket now listening'

def clientThread(conn):
        print "WAITING.........."
        try:
                 while True: 
                        data = conn.recv(1024)
                        print data
                        if data=="1": # command "1" will turn on pin 13 led
                                ser.write("1")
                                confirm = ser.readline()
                                #client_sock.send(confirm)
                                conn.sendall(confirm+"\n")
                                print confirm
                        if data == "0": # command "0" will turn off pin 13 led
                                ser.write("0")
                                confirm = ser.readline()
                                #client_sock.send(confirm)
                                conn.sendall(confirm+"\n")
                                print confirm
                        if data == "2": # command "2" will close the connection
                                print "connection closed"
                                ser.close()
                                conn.sendall('connection closed')
                                conn.close()
                                break
        except:
                ser.close()
                conn.close()
while True:
        conn,addr = s.accept()
        print "connected with "+addr[0]+":"+str(addr[1])
        start_new_thread(clientThread,(conn,))
s.close()
