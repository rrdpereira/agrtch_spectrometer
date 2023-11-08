###############################################################################################################
# spectrometer_lib_ND_CSV_UTC_M_FLMS04727.py

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
Dots1Inch_height = 96
Dots1Inch_width = 96
###############################################################################################################
def main():
    SerialFLMS = 'FLMS04727'

    # # Chechk part
    # print("SerialFLMS: {0}".format(SerialFLMS))

    # for i in range(100):
    #     fout = i + 10
    #     print("fout727: {0}".format(fout))

    specs = Spectrometer.from_serial_number(SerialFLMS)
    specs.integration_time_micros(5000)  # Integration time in microseconds (us)
    try:
        while True:
            wave, ints = specs.spectrum()
            filename = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y%m%d_%H%M%S") + "_" + SerialFLMS
            # # Filename 01
            # np.savetxt(filename + ".csv", np.vstack((wave, ints)).T, delimiter=', ')
            # Filename 02
            # Save the data to a CSV file with comments for x and y labels
            with open(filename + ".csv", "w") as file:
                file.write("Wavelength[nm], Intensity[16bits_65535_0]\n")  # Manually insert your x and y labels
                np.savetxt(file, np.vstack((wave, ints)).T, delimiter=', ')
    except KeyboardInterrupt:
        # Exit on CTRL-C
        pass
###############################################################################################################
if __name__ == '__main__':
    main()
###############################################################################################################    