from ProcessLogic import *
# This is the main file to call from the terminal
if  __name__ == "__main__":
    #User Interaction
    while True:
        print('Please define the end temperature in the tank in Celcius (This should between 20 - 60 Celsius)')
        temp_thresh=input()
        if temp_thresh<'20' or temp_thresh>'60':
            try:
                temp_thresh=float(temp_thresh)
                break
            except:
                continue
        else:
            continue 

    while True:
        print('Please define the threshold for the ph-value')
        ph_value_thresh=input()
        if temp_thresh<='14' or temp_thresh>='0':
            try:
                ph_value_thresh=float(ph_value_thresh)
            except ValueError:
                continue
        else: 
            continue
    
    messdaten,ph_value=processLogic(temp_thresh=temp_thresh,ph_value_thresh=ph_value_thresh)

    print("Process End")
    print('Temperature in Celsius = ', messdaten)
    print('pH-value = ', ph_value)

