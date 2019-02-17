import serial
portName = '/dev/cu.usbmodem1411'

ser = serial.Serial(portName, 9600)

f = open('log.csv', 'a')

while True:
    f.write(str(ser.readline()))
    f.close()
    f = open('log.csv','a')