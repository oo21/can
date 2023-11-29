# reset the counter for odometer and let the speed equal zero
import time
import os

def start():
    ti = time.time()
    f = open("start_monitoring.txt","a")
    f.write(f"start:,{ti}\n")

def end():
    ti = time.time()
    f = open("start_monitoring.txt","a")
    f.write(f"start:,{ti}\n")

while 1:
    s = input('[s]tart?: ')
    if s == 's':
        start()
        
    if s == 'e':
        end()
