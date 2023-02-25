from seabreeze.spectrometers import list_devices, Spectrometer
from re import search

devices = str( list_devices())
print(devices)

substring = "4868"
if search(substring, devices):
    print ("FLMS04868")
else:
    print ("FLMS04767")




# index = devices.find('4868')
# if index != -1:
#     print("4868 OK: ", index)
# else:
#     print('NOK')