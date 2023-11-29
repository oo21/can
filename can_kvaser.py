import time
import can

bustype = 'socketcan'
channel = 'can0'

bus = can.Bus(channel = channel, interface = bustype)

while 1:
    dta = bus.recv()
    print(f"pid = {dta.arbitration_id} data = {dta.data} length = {dta.dlc}")

"""
ch1 = canlib.openChannel(channel=0)
ch1.setBusParams(canlib.canBITRATE_500K)
ch1.busOn()

frame = Frame(id_=2015, data = bytearray(b'\x01\x03\x0D\xAA\xAA\xAA\xAA\xAA'),flags = canlib.MessageFlag.STD)

#ch1.writeWait(frame,timeout=5000)

print(ch1.read())
"""
