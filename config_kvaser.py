import os
brate_choice = int(input("choose baud rate [1] 500000  [2] 100000 bps:"))
if brate_choice == 1:
    baudrate = 500000
elif brate_choice == 2:
    baudrate = 100000

com = f"ip link set can0 up type can bitrate {baudrate} dbitrate 3000000 fd on fd-non-iso on"

os.system(com)
