import subprocess
import serial
import time
import os

def checkPumpSpeed(index):
    label = subprocess.getstatusoutput("reg query HKEY_CURRENT_USER\SOFTWARE\HWiNFO64\VSB /v Label" + index)

    sensor = float(label[1].split('   ')[3].strip())

    if (sensor != "AIO Pump"):
        os.system('shutdown /s /t 1')
    
    data = subprocess.getstatusoutput("reg query HKEY_CURRENT_USER\SOFTWARE\HWiNFO64\VSB /v ValueRaw" + index)

    speed = float(data[1].split('   ')[3].strip())
    
    if (speed < 1500):
        os.system('shutdown /s /t 1')


def getSSDTemp(index):
    data = subprocess.getstatusoutput("reg query HKEY_CURRENT_USER\SOFTWARE\HWiNFO64\VSB /v ValueRaw" + index)

    temp = float(data[1].split('   ')[3].strip())

    return temp

def getMemJunct(index):
    data = subprocess.getstatusoutput("reg query HKEY_CURRENT_USER\SOFTWARE\HWiNFO64\VSB /v ValueRaw" + index)

    temp = float(data[1].split('   ')[3].strip())

    return temp
    
def main():
    while 1:
        try:
            checkPumpSpeed("0")
        except:
            os.system('shutdown /s /t 1')
            
        try:
            
            ssd = getSSDTemp("1")
            gpu = getMemJunct("2")
            highest = int(max(ssd, gpu)) - 50

            if highest < 10:
                setPwm = 60
            else:
                setPwm = round(highest * 6.375)
            
            if setPwm > 255:
                setPwm = 255
            elif setPwm < 60:
                setPwm = 60
        
        except:
            setPwm = 100
        
        setPwm = str(setPwm)
        
        arduino.write(bytes(setPwm, 'utf-8'))
        time.sleep(0.25)
        data = arduino.readline()
        print(data)  
    
arduino = serial.Serial(port = 'COM3', baudrate=9600, timeout = 2) 
if __name__ == "__main__":
    main()

