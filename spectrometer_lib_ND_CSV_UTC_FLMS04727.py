###############################################################################################################
# spectrometer_lib_ND_CSV_UTC_FLMS04727.py

# Created by: Robson Rogério Dutra Pereira on 01.Sep.2023
# Last Modified: rrdpereira

# Description: USB spectrometer CSV datalogger of serial number "FLMS0xxxx".

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
if __name__ == '__main__':
    SerialFLMS='FLMS04727'
    specs=Spectrometer.from_serial_number(SerialFLMS)
    # print(f"(Spectrometer) :: {specs} ::")

    specs.integration_time_micros(5000) # Integration time in microseconds (us)

    wavelen=specs.wavelengths()
    # print(f"(Wavelengths) :: {wavelen} ::")

    intens=specs.intensities()
    # print(f"(Intensities) :: {intens} ::")

    try:
        while True:
            wave,ints=specs.spectrum()
            np.savetxt(datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")+"_"+SerialFLMS+".csv", np.vstack((wave,ints)).T, delimiter=', ')
    except KeyboardInterrupt:
        # Exit on CTRL-C
        pass            
###############################################################################################################    