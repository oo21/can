import time
import serial

ser = serial.Serial('/dev/ttyUSB0',baudrate = 921600)

def enter_config_mode(ser):
	ser.write(b"+++")
	time.sleep(0.3)
	ser.write(b"AT\r")


def do_config_can_interface_module_commands(ser):
	ser.write(b"AT\r")
	time.sleep(0.1)
	ser.write(b"AT+CAN=500,7DF,NDTF\r")
	time.sleep(0.1)
	ser.write(b"AT+UART=921600,8,1,NONE,NFC\r")
	time.sleep(0.1)
	ser.write(b"AT+MODE=PROTOL\r")


def exit_config_mode(ser):
	ser.write(b"AT+EXAT\r")


def reset_can_interface(ser):
	"this is needed after configuration in order for the module to take the configurations"
	ser.write(b"AT+REBT\r")


def do_all_configuration(ser):
	enter_config_mode(ser)
	time.sleep(0.1)
	do_config_can_interface_module_commands(ser)
	time.sleep(0.1)
	exit_config_mode(ser)
	time.sleep(0.1)
	reset_can_interface(ser)

"""
def read_obd_data(pid,ser):
	External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x02\x01\x0D\xAA\xAA\xAA\xAA\xAA') ### this is the original byte array
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x01\x03\x00\xAA\xAA\xAA\xAA\xAA')
	External_IO[7] = pid
	print(External_IO)
	ser.write(External_IO)
	data = ser.read(13)
	return data
"""

def read_obd_data(pid,ser):
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x02\x01\x0D\xAA\xAA\xAA\xAA\xAA') ### this is the original byte array
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x01\x03\x00\xAA\xAA\xAA\xAA\xAA')
	#External_IO[7] = pid
	#print(External_IO)
	#ser.write(External_IO)
	data = ser.read(13)
	return data



def write_all_pytes():
	External_IO = bytearray(b"\x08\x00\x00\x07\xdf\x02\x01\x0c\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\r\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x05\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x0f\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x10\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x0b\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x11\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x0e\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01\x04\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01/\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01D\xaa\xaa\xaa\xaa\xaa\x08\x00\x00\x07\xdf\x02\x01o\xaa\xaa\xaa\xaa\xaa") ### this is the original byte array
	ser.write(External_IO)

def read_obd_data2(ser):
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x02\x01\x0D\xAA\xAA\xAA\xAA\xAA') ### this is the original byte array
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x01\x03\x00\xAA\xAA\xAA\xAA\xAA')
	#External_IO[7] = pid
	#print(External_IO)
	#ser.write(External_IO)
	data = ser.read(13)
	return data



def read_obd_dtc(pid,ser):
	#External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x02\x01\x0D\xAA\xAA\xAA\xAA\xAA') ### this is the original byte array
	External_IO = bytearray(b'\x08\x00\x00\x07\xDF\x01\x03\x00\xAA\xAA\xAA\xAA\xAA')
	External_IO[7] = pid
	ser.write(External_IO)
	data = ser.read(13)
	return data


def byte_array_to_binary(ba):
    bab = []
    for i in ba:
      bab.append(f"{bin(i)[2:].zfill(8)} ")
    return("".join(bab))


def read_speed(ser):
	"""this function returns the vehicle speed in km/h"""
	data = ser
	speed = data[8] #"speed in [km/h]
	return speed


def read_rpm(ser):
	data = ser
	rpm_bytes = data[8:10]
	rpm = int.from_bytes(rpm_bytes,'big')*0.25
	#strrpm = f"{hex(data[8])}{hex(data[9])}"
	#rpm = 0.25 * int(strrpm)
	return rpm
	#return int(str(rpm)[1:],16) 


def read_engine_coolant_temp(ser):
	data = ser
	tmp = data[8] -40 
	return tmp


def read_intake_air_temp(ser):
	data = ser
	tmp = data[8] -40 
	return tmp


def read_intake_air_flow(ser):
	data = ser
	# print(byte_array_to_binary(data))
	#flow = int.from_bytes(data[8:10],'big')*0.01
	flow = (256*data[8] + data[9])/100 
	return flow


def read_intake_air_abs_pressure(ser):
	data = ser
	pressure = data[8] 
	return pressure


def read_abs_throttle_pos(ser):
	data = ser
	pos = data[8]*(100/255) 
	return pos


def read_ignition_timing_advance(ser):
	data = ser
	#print(byte_array_to_binary(data))
	deg = (data[8]) - 64*2
	return deg


def read_calculated_load_value(ser):
	data = ser
	#print(byte_array_to_binary(data))
	load = data[8] /2.55
	return load


def read_fluel_level(ser):
	data = ser
	#print(byte_array_to_binary(data))
	lvl = data[8] *(100/255)
	return lvl


def read_air_fuel_equivelance_ration(ser):
	data = ser
	#print(byte_array_to_binary(data))
	#rat = (2/65536)*(256*data[7] + data[9])
	rat = data[8]
	return rat


def read_turbo_pressure(ser):
	data = ser
	#print(byte_array_to_binary(data))
	tpress = (data[8]-1)/2
	return tpress


def read_dtc(n1,n2,ser):
	# handle when there is no dtcs 
	data = ser
	bin_list = (byte_array_to_binary(data)).split(" ")
	#print(bin_list)
	fc = bin_list[8][:2]
	if fc =="00":
		c1 = 'P'
	elif fc == "01":
		c1="C"
	elif fc == "10":
		c1 = "B"
	elif fc == "11":
		c1 = "U"
	c2 = int(bin_list[n1][2:4],2)
	c3 = int(bin_list[n1][4:] ,2)
	c4 = int(bin_list[n2][0:4],2)
	c5 = int(bin_list[n2][4:] ,2)
	dtc = f"{c1}{c2}{c3}{c4}{c5}"
	return dtc


if __name__ == '__main__' and False:
	while 1:
		#time.sleep(0.05)
		#print(f"speed = {read_speed()}")
		write_all_pytes()
		print(f"""
rpm: 	{read_rpm(ser)					}
speed:  {read_speed(ser)				}
ec tmp: {read_engine_coolant_temp(ser)				}
ia tmp: {read_intake_air_temp(ser)					}
iaflow: {read_intake_air_flow(ser)					}
press:  {read_intake_air_abs_pressure(ser)			}
pos:	{read_abs_throttle_pos(ser)				}	
deg:	{read_ignition_timing_advance(ser)			}
load:	{read_calculated_load_value(ser)			}
lvl:	{read_fluel_level(ser)						}
rat:	{read_air_fuel_equivelance_ration(ser)		}
tpress: {read_turbo_pressure(ser)					}
DTC	:	read_dtc(8,9,ser)		read_dtc(10,11,ser)
""")


test = True

if test:
	while 1:
		write_all_pytes()
		time.sleep(0.025)
		dt = ser.read_all()
		#print(dt)
		#time.sleep(0.05)
		data1 = dt[:13]					
		data2 = dt[13:26]		
		data3 = dt[26:39]			
		data4 = dt[39:52]			
		data5 = dt[52:65]			
		data6 = dt[65:78]		
		data7 = dt[78:91]					
		data8 = dt[91:104]		
		data9 = dt[104:117]		
		data10 =dt[117:130]
		data11 =dt[130:143]	
		data12 =dt[143:156]				



		print(f"""
rpm: 	{read_rpm(data1)					}
speed:  {read_speed(data2)				}
ec tmp: {read_engine_coolant_temp(data3)				}
ia tmp: {read_intake_air_temp(data4)					}
iaflow: {read_intake_air_flow(data5)					}
press:  {read_intake_air_abs_pressure(data6)			}
pos:	{read_abs_throttle_pos(data7)				}	
deg:	{read_ignition_timing_advance(data8)			}
load:	{read_calculated_load_value(data9)			}
lvl:	{read_fluel_level(data10)						}
rat:	{read_air_fuel_equivelance_ration(data11)		}
tpress: {read_turbo_pressure(data12)					}
DTC	:	read_dtc(8,9,ser)		read_dtc(10,11,ser)
""")

#		print(
"""
	rpm: 	{data1 }
	speed:  {data2 }
	ec tmp: {data3 }
	ia tmp: {data4 }
	iaflow: {data5 }
	press:  {data6 }
	pos:	{data7 }	
	deg:	{data8 }
	load:	{data9 }
	lvl:	{data10}
	rat:	{data11}
	tpress: {data12}

	"""


#ba = [0x08,0x00,0x00,0x07,0xDF,0x02,0x01,0x0C,0x55,0x55,0x55,0x55,0x55]
# External_IO = bytearray(13)
# print(External_IO)
# External_IO[0] = 0x08 
# External_IO[1] = 0x00 
# External_IO[2] = 0x00 
# External_IO[3] = 0x07 
# External_IO[4] = 0xDF 
# External_IO[5] = 0x02 
# External_IO[6] = 0x01 
# External_IO[7] = 0x0D 
# External_IO[8] = 0xAA 
# External_IO[9] = 0xAA 
# External_IO[10]= 0xAA
# External_IO[11]= 0xAA
# External_IO[12]= 0xAA