###############################################################################################################
# spectrometer_lib_FLMS04868.py

# Created by: Robson Rogério Dutra Pereira on 01.Sep.2023
# Last Modified: rrdpereira

# Description: USB spectrometer CSV and PNG datalogger with delay of serial number "FLMS0xxxx".

# E-mail: robsondutra.pereira@outlook.com
###############################################################################################################
import sys, time, os, datetime
current_file_name = os.path.splitext(os.path.basename(__file__))[0]
print("current_file_name: {0}".format(current_file_name))
###############################################################################################################
from seabreeze.spectrometers import list_devices, Spectrometer
from re import search
import matplotlib.pyplot as plt
import numpy as np
###############################################################################################################
from platform import python_version
print(f"(Sys version) :|: {sys.version} :|:")
os.system("which python")
print(f"(Python version) :#: {python_version()} :#:")
###############################################################################################################
Dots1Inch_height=96
Dots1Inch_width=96

if __name__ == '__main__':
    SerialFLMS='FLMS04868'
    specs=Spectrometer.from_serial_number(SerialFLMS)
    # print(f"(Spectrometer) :: {specs} ::")

    specs.integration_time_micros(5000) # Integration time in microseconds (us)

    wavelen=specs.wavelengths()
    # print(f"(Wavelengths) :: {wavelen} ::")

    intens=specs.intensities()
    # print(f"(Intensities) :: {intens} ::")

    # plot the acquired spectrum
    plt.ion()
    try:
        while True:
            wave,ints=specs.spectrum()
            np.savetxt(time.strftime("%Y%m%d_%H%M%S")+"_"+SerialFLMS+".csv", np.vstack((wave,ints)).T, delimiter=', ')
            plt.title(SerialFLMS+"_"+time.strftime("%Y%m%d_%H%M%S"))
            plt.plot(wave,ints)
            # 1 second to save PNG file
            plt.savefig(time.strftime("%Y%m%d_%H%M%S")+"_"+SerialFLMS+".png",format="png",dpi=Dots1Inch_height)
            plt.cla()
            time.sleep(1) # Sleep for 1 second            
    except KeyboardInterrupt:
        # Exit on CTRL-C
        pass            
###############################################################################################################    