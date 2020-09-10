import serial

letter = input("Prefix letter: ").upper()

for i in range(int(input("Starting unit: ")),9999):
        input("")
        with serial.Serial('/dev/ttyUSB0', 38400, timeout=1) as ser:
                print("Setting Device Name...")
                ser.write(f"AT+NAME={letter}{str(i).zfill(4)}\r\n".encode())
                print(ser.read(10).decode())
                print("Setting Device PIN...")
                ser.write(b"AT+PSWD=0000\r\n")
                print(ser.read(10).decode())
                print("Setting Device Baud Rate...")
                ser.write(b"AT+UART=9600,0,0\r\n")
                ser.write(b"AT+BAUD4\r\n")
                print(ser.read(10).decode())
                print("Setting Device Role...")
                ser.write(b"AT+ROLE=0\r\n")
                print(ser.read(10).decode())
                print(f"Device {letter}{str(i).zfill(4)} finished")
