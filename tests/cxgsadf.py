from seabreeze.spectrometers import list_devices, Spectrometer
from re import search
import matplotlib.pyplot as plt
import numpy as np

import sys, time, os, datetime
os.system("which python")
print(sys.version)
from platform import python_version
print(python_version())

Dots1Inch_height=96
Dots1Inch_width=96

# Spectrometer.open()
# devices = str( list_devices())
# print(devices)

specs=Spectrometer.from_serial_number('FLMS04868')
print(specs)

specs.integration_time_micros(5000)

wavelen=specs.wavelengths()
print(wavelen)

intens=specs.intensities()
print(intens)

wave,ints=specs.spectrum()

np.savetxt(time.strftime("%Y%m%d_%H%M%S")+"_FLMS04727"+".csv", np.vstack((wave,ints)).T, delimiter=', ')
plt.title("FLMS04727_"+time.strftime("%Y%m%d_%H%M%S"))
plt.plot(wave,ints)
plt.pause(5)
plt.savefig(time.strftime("%Y%m%d_%H%M%S")+"_FLMS04727"+".png",format="png",dpi=Dots1Inch_height)
plt.cla()

# Spectrometer.close()

# substring = "4868"
# if search(substring, devices):
#     print ("FLMS04868")
# else:
#     print ("FLMS04767")




# index = devices.find('4868')
# if index != -1:
#     print("4868 OK: ", index)
# else:
#     print('NOK')