import can
import time


class Can_Bus():

    bustype = 'socketcan'
    channel = 'can0'

    bus = can.Bus(channel = channel, interface = bustype)

class Classifier():
    bustype = 'socketcan'
    channel = 'can0'
    bus = can.Bus(channel = channel, interface = bustype)

    def decode_speed(self, data):
        speed = (data[3]/2)*0.1
        return speed

    def calculate_trip_distance_from_speed(self,d0,speed,td): # calibrate speed in order for this function to be accurate
        distance = d0+((speed*1000)/3600)*td
        print(d0,speed,distance,td)
        return distance
    

    def decode_front_doors_status(self, data): 
        if data[1] == 0x40 or data[1] == 0x50: # need edit
            fl = "closed"
        elif data[1] == 0x41 or data[1] == 0x51: # need edit
            fl = "opend"
        else:
            fl = "uk"
        if data[4] == 0x00 or data[4] == 0x01: # need edit
            fr = "closed"
        elif data[4] == 0x08 or data[4] == 0x09: # need edit
            fr = "opend"
        else:
            fr = "uk"
        return fl,fr



    def decode_rear_doors_status(self, data): # check if need edit
        if data[3] == 0x00: 
            rl = "closed"
        elif data[3] == 0x01:
            rl = "opend"
        if data[2] == 0x00:
            rr = "closed"
        elif data[2] == 0x80:
            rr = "opend"
        return rl,rr

    def decode_light_status(self, data): # check if need edit
        if data[3] == 0x00:
            ls = "off"
        elif data[3] == 0x80:
            ls = "on"
        return ls

    def decode_brake_power(self, data):
        power = data[0]*(100/130)
        return power

    def decode_gas_power(self, data):
        power = data[1] * (100/102)
        return power

    def decode_ssteering_angle_torque(self, data):
        ang = data[0]
        ang1 = data[1]
        torque = data[2]
        if ang1 > 230:
            ang3 = ((ang-255)+((ang1-255)*255))/10  
        else:  
            ang3 = (ang+ang1*255)/10
        return ang3,torque

    def decode_trip_distance(self,data,odo0,td0):
        if data[0] != odo0:
            distance = td0 + 100
        return distance

class RET(): # reverse engineering tool

    def pehaviour(pid):
        pass                


a_classifier = Classifier()

def main(a_classifier):
    counter = 0
    while 1:
        #time.sleep(0.000001)
        dta = a_classifier.bus.recv()
        if counter == 0:
            print("innnnnnnnnnnnnnn")
            t0 = time.time()
            d0 = 0
            odo0 = 0
            td0 = 0
            counter+=1
            continue

        #print(dta.data)
        if dta.arbitration_id == 0x56B:
            a_classifier.speed = a_classifier.decode_speed(dta.data)
            tn = time.time()
            td = tn - t0
            a_classifier.distance = a_classifier.calculate_trip_distance_from_speed(d0,a_classifier.speed,td)
            d0 = a_classifier.distance
            t0 = tn
        if dta.arbitration_id == 0x5d0:
            a_classifier.trip_distance = a_classifier.decode_trip_distance(dta.data,odo0)
            td0 = a_classifier.trip_distance
        if dta.arbitration_id == 0x541:
            a_classifier.fl,a_classifier.fr = a_classifier.decode_front_doors_status(dta.data)
        if dta.arbitration_id == 0x553:
            a_classifier.rl,a_classifier.rr = a_classifier.decode_rear_doors_status(dta.data)
        if dta.arbitration_id == 0x541:
            a_classifier.ls = a_classifier.decode_light_status(dta.data)
        if dta.arbitration_id == 0x331:
            a_classifier.prake_power = a_classifier.decode_brake_power(dta.data)
        if dta.arbitration_id == 0x230:
            a_classifier.gas_power = a_classifier.decode_gas_power(dta.data)
        if dta.arbitration_id == 0x2B0:    
            a_classifier.sa,a_classifier.st= a_classifier.decode_ssteering_angle_torque(dta.data)

        #if counter > 500:
            #print(f"speed ; {speed}  distance {distance} fl,fr {fl,fr}   rl,rr  {rl,rr}  ls {ls} prake_power {prake_power:.2f} gas_power {gas_power:.2f} sa,st = {sa,st}")
        counter +=1

if __name__ == "__main__":
    main()