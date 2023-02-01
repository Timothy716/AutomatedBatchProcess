import Adafruit_ADS1x15
from PlugConnection import *

def processLogic(temp_thresh,ph_value_thresh):
    #calculate the threshold for the ph-sensor
    #Factors for the ph-function
    a=3700.0
    b=-10667.0
    ph_value_thresh=a*ph_value_thresh+b
    print("The value for the sensor is = ",ph_value_thresh)

    #turn off all plugs --> safe mode
    heater_on,stirrer_on,pump_on=enterSaveMode()

    # Create an ADS1115 ADC (16-bit) instance
    adc = Adafruit_ADS1x15.ADS1115() 
    GAIN = 1

    #check the initial conditions
    # Start the stirrer
    stirrerON()

    messdaten = aktuelleTemperatur()
    ph_value= adc.read_adc(0, gain=GAIN) # Read the ADC channel 0 value
    messdaten=float(messdaten)
    ph_value=float(ph_value)

    if messdaten <= temp_thresh:
        #plug heater on 
        heaterON()
        heater_on =True
    if ph_value>=ph_value_thresh:
        #plug pump on 
        pumpON()
        pump_on=True

    #To stop the remote from sending 
    stop_send_pump=False 
    stop_send_heater=False 

    while heater_on == True or pump_on == True:
        
    #Check the temperature
        messdaten = aktuelleTemperatur()
        ph_value= adc.read_adc(0, gain=GAIN) # Read the ADC channel 0 value
        messdaten=float(messdaten)
        ph_value=float(ph_value)
        
        print("temperature", messdaten)
        print("pH Value",((ph_value+b)/a))
        
        if messdaten >= 0.9*temp_thresh:
            
        #plug heater off 
            heater_on =False
            if heater_on ==False and stop_send_heater==False:
            #Turn off plug heater
                heaterOFF()
                stop_send_heater=True

        if ph_value<=ph_value_thresh:
            
        #plug pump off 
            pump_on=False
            if pump_on ==False and stop_send_pump==False: 
                #Turn off plug pump
                pumpOFF()
                stop_send_pump=True


    #reach the threshold due to thermal inertia 
    messdaten = aktuelleTemperatur()
    messdaten=float(messdaten)
    if messdaten <= temp_thresh:
        heater_on =True  
        #plug heater on 
    # os.system("cd /home/pi/raspberry-remote; ./send 10101 1 1")
        while heater_on==True:
            messdaten = aktuelleTemperatur()
            messdaten=float(messdaten)
            print("temperature", messdaten)
            print("pH Value",((ph_value+b)/a))
            if messdaten >= temp_thresh:
            #    os.system("cd /home/pi/raspberry-remote; ./send 10101 1 0")
                heater_on =False
            #Turn off plug

    # turn off stirrer     
    stirrerOFF()

    #safe mode --> turn off all plugs
    heater_on,stirrer_on,pump_on=enterSaveMode()


    #convert the value from the sensor into a ph-value 
    ph_value=(ph_value+b)/a
    return messdaten,ph_value


