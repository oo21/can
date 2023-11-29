import PySimpleGUI as sg
import can_communication_copy as cc
import serial

NAME_SIZE = 23

def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')



layout = [[name('Port'),sg.OptionMenu(['ttyUSB0','ttyUSB1'],default_value='ttyUSB0',s=(15,2),k='ops')],
          [name('Configuration'), sg.Button('Configure_Can_Interface')],
          [sg.Text('',font='_ 14')],
          [sg.Text('',font='_ 14', k='rpm')],
          [sg.Text('',font='_ 14', k='speed')],
          [sg.Text('',font='_ 14', k='ct')],
          [sg.Text('',font='_ 14', k='iat')],
          [sg.Text('',font='_ 14', k='iaf')],
          [sg.Text('',font='_ 14', k='iap')],
          [sg.Text('',font='_ 14', k='atp')],
          [sg.Text('',font='_ 14', k='ita')],
          [sg.Text('',font='_ 14', k='clv')],
          [sg.Text('',font='_ 14', k='fl')],
          [sg.Text('',font='_ 14', k='afe')],
          [sg.Text('',font='_ 14', k='tb')],
          [sg.Text('',font='_ 14', k='dtc')],
]
window = sg.Window(title=" obd data " ,layout=layout)
counter = 0

# window['rpm'].update("new_text") # (f"{counter}")
while 1:
    counter+=1
    event,values = window.read(timeout=1)
    #port = values['ops']
    try:
        #ser = serial.Serial(f"/dev/{port}",baudrate = 921600,timeout=0.1)
        ser = cc.ser
    except:
        print("not valid port")
        continue
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event=="Configure_Can_Interface":
        print("configure pressed")
        cc.do_all_configuration(ser)
    else:
        try:
            window['rpm'].update(f'rpm\t\t\t\t{int(cc.read_rpm(ser))}')               
            window['speed'].update(f'speed\t\t\t\t{int(cc.read_speed(ser))}')
            window['ct'].update(f'engine coolant temp\t\t\t{int(cc.read_engine_coolant_temp(ser))}')
            window['iat'].update(f'intake air temp\t\t\t{int(cc.read_intake_air_temp(ser))}')
            window['iaf'].update(f'intake air flow\t\t\t{int(cc.read_intake_air_flow(ser))}')
            window['iap'].update(f'intake air abs pressure\t\t{int(cc.read_intake_air_abs_pressure(ser))}')
            window['atp'].update(f'abs throttle pos\t\t\t{int(cc.read_abs_throttle_pos(ser))}')
            window['ita'].update(f'ignition timing advance\t\t{int(cc.read_ignition_timing_advance(ser))}')
            window['clv'].update(f'calculated load value\t\t{int(cc.read_calculated_load_value(ser))}')
            window['fl'].update(f'fluel level\t\t\t\t{int(cc.read_fluel_level(ser))}')
            window['afe'].update(f'air fuel equivelance ratio\t\t{int(cc.read_air_fuel_equivelance_ration(ser))}')
            #window['tb'].update(f'turbo pressure\t\t\t{int(cc.read_turbo_pressure(ser))}')
            #window['dtc'].update(f'dtc\t\t\t\t{int(cc.read_dtc(8,9,ser))}')
            #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        except:
            print("not valid port")
            
        #print(type(values['ops']))
        
        #print(counter)
    #window.close()
