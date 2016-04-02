import bluetooth
import serial
print "android to arduino// waiting for connection"
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = bluetooth.PORT_ANY
server_sock.bind(("",port))
server_sock.listen(1)

bluetooth.advertise_service(server_sock,"",service_classes=[bluetooth.SERIAL_PORT_CLASS],profiles=[bluetooth.SERIAL_PORT_PROFILE])
client_sock, address = server_sock.accept()
print "accepted connection from",address
ser = serial.Serial('COM3',9600)
try:
    while(True):
        data = client_sock.recv(1024)
        if data=="1":
            ser.write('1')
            confirm = ser.readline()
            client_sock.send(confirm)
            print confirm
        if data=="0":
            ser.write('0')
            confirm = ser.readline()
            client_sock.send(confirm)
            print confirm
        if data=="2":
            ser.close()
            client_sock.send("connection closed\n")
            client_sock.close()
            server_sock.close()
            break

    print "#connection closed"
except:
    ser.close()
    
    
