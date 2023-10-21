###############################################################################################################
# spectrometer_lib_ND_UTC_M_FLM_main.py

# Created by: Robson Rogério Dutra Pereira on 01.Sep.2023
# Last Modified: rrdpereira

# Description: Spectrometer main call for the two units.

# E-mail: robsondutra.pereira@outlook.com
###############################################################################################################
import spectrometer_lib_ND_UTC_M_FLMS04727
import spectrometer_lib_ND_UTC_M_FLMS04868
import gc, time
from datetime import datetime
import threading
###############################################################################################################
def run_main_function(module):
    module.main()
###############################################################################################################
thread1 = threading.Thread(target=run_main_function, args=(spectrometer_lib_ND_UTC_M_FLMS04727,))
thread2 = threading.Thread(target=run_main_function, args=(spectrometer_lib_ND_UTC_M_FLMS04868,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
###############################################################################################################