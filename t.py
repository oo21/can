import time
import serial

ser = serial.Serial('/dev/ttyUSB0',baudrate = 921600)


def read_obd_data(pid):
	External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x02\x01\x0D\xAA\xAA\xAA\xAA\xAA') ### this is the original byte array
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x01\x03\x00\xAA\xAA\xAA\xAA\xAA')
	External_IO[7] = pid
	#print(External_IO)
	ser.write(External_IO)
	data = ser.read(13)
	return data

while 1:
    t0 = time.time()
    #read_obd_data(0x0D)
    ser.write(bytearray(b'\x08\x00\x00\x07\xdf\x02\x01\r\xaa\xaa\xaa\xaa\xaa'))
    data = ser.read(13)
    tf = time.time()
    print(f"time = {tf-t0}")