from seabreeze.spectrometers import list_devices, Spectrometer
from re import search
import matplotlib.pyplot as plt
import numpy as np

import sys, time, os, datetime
from platform import python_version

print(f"(Sys version) :|: {sys.version} :|:")
os.system("which python")
print(f"(Python version) :#: {python_version()} :#:")

Dots1Inch_height=96
Dots1Inch_width=96

if __name__ == '__main__':
    SerialFLMS='FLMS04868'
    specs=Spectrometer.from_serial_number(SerialFLMS)
    print(f"(Spectrometer) :: {specs} ::")

    specs.integration_time_micros(1000) # Integration time in microseconds (us)

    wavelen=specs.wavelengths()
    print(f"(Wavelengths) :: {wavelen} ::")

    intens=specs.intensities()
    print(f"(Intensities) :: {intens} ::")

    # plot the acquired spectrum
    plt.ion()
    try:
        while True:
            wave,ints=specs.spectrum()
            np.savetxt(time.strftime("%Y%m%d_%H%M%S")+"_"+SerialFLMS+".csv", np.vstack((wave,ints)).T, delimiter=', ')
            plt.title(SerialFLMS+"_"+time.strftime("%Y%m%d_%H%M%S"))
            plt.plot(wave,ints)
            plt.pause(2) # Sample time in seconds (s)
            plt.savefig(time.strftime("%Y%m%d_%H%M%S")+"_"+SerialFLMS+".png",format="png",dpi=Dots1Inch_height)
            plt.cla()
    except KeyboardInterrupt:
        # Exit on CTRL-C
        pass            