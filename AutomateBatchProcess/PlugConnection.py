import os

def aktuelleTemperatur():
      
    # 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-01144a4213aa/w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000

    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

def enterSaveMode():
    #turn off all plugs 
    #plug for the heater
    os.system("cd /home/pi/raspberry-remote; ./send 10101 1 0")
    heater_on=False
    #plug for the stirrer
    os.system("cd /home/pi/raspberry-remote; ./send 10101 2 0")
    stirrer_on=False
    #plug for the pump
    os.system("cd /home/pi/raspberry-remote; ./send 10101 3 0 ")
    pump_on=False
    return heater_on,stirrer_on,pump_on

def stirrerON():
    #plug stirrer on 
    os.system("cd /home/pi/raspberry-remote; ./send 10101 2 1")

def heaterON():
    #plug heater on 
    os.system("cd /home/pi/raspberry-remote; ./send 10101 1 1")

def pumpON():
    #plug pump on 
    os.system("cd /home/pi/raspberry-remote; ./send 10101 3 1")

def heaterOFF():
    #Turn off plug heater
    os.system("cd /home/pi/raspberry-remote; ./send 10101 1 0")

def pumpOFF():
    #Turn off plug pump
    os.system("cd /home/pi/raspberry-remote; ./send 10101 3 0")

def stirrerOFF():
    #Turn off stirrer
    os.system("cd /home/pi/raspberry-remote; ./send 10101 2 0")


