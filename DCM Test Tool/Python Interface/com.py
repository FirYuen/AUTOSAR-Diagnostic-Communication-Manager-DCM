#com

from parameters import *
import serial
import serial.tools.list_ports

# Check connection
def KeepAlive():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if (port.description[:29] == com_device_name):
            return (True, port.device)
    else: return (False, 0)

# Update SerState
def UpdateSerState():
    global serState
    serState = KeepAlive()
    return serState[0]

# Send Byte
def SendByte(byte):
    try:
        ser.write(byte)
        counter += 1
        print('{:5d}'.format(counter), ": Sent Byte =", byte)
    except serial.SerialException:
        print("Connection Lost!")
        input("Press 'Enter' to exit ")
        exit()

def EstablishConnection():
    global ser, TX_counter, RX_counter
    
    TX_counter, RX_counter = 0, 0
    
    try:
        ser = serial.Serial(serState[1], com_baudrate, timeout=0)
        print(">> MESSAGE: Successful connection!")
        return True
    except serial.SerialException:
        print(">> MESSAGE (ERR): Connection Failed!")
        return False
    
def GetComPort():
    return serState[1]

