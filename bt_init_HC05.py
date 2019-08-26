import serial

for i in range(int(input("Starting unit: ")),9999):
	input("")
	with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
		ser.write(f"AT+NAMEA{str(i).zfill(4)}\r\n".encode())
		print(ser.read(10).decode())
		print(f"Device A{str(i).zfill(4)} finished")

