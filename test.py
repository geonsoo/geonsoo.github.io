import serial
portName = '/dev/cu.usbmodem1411'

ser1 = serial.Serial(portName, 9600)

while True:
	print (ser1.readline())