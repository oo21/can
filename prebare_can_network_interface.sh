#sudo slcand -o -s6 -t hw -S 3000000 /dev/mhydra0 -F
sleep 2s
ip link set can0 up type can bitrate 100000 dbitrate 3000000 fd on fd-non-iso on
#sudo ip link set up can0
