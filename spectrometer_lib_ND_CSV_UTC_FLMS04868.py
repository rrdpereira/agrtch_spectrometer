from seabreeze.spectrometers import list_devices, Spectrometer
from re import search
import numpy as np

import sys, time, os, datetime
from platform import python_version

# print(f"(Sys version) :|: {sys.version} :|:")
os.system("which python")
# print(f"(Python version) :#: {python_version()} :#:")

if __name__ == '__main__':
    SerialFLMS='FLMS04868'
    specs=Spectrometer.from_serial_number(SerialFLMS)
    # print(f"(Spectrometer) :: {specs} ::")

    specs.integration_time_micros(1000) # Integration time in microseconds (us)

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