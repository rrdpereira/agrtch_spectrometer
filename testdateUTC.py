import time, datetime

# # Mode 01
# aaaa = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
# print(aaaa)

# Mode 02
try:
    while True:
        print(datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y%m%d_%H%M%S"))
        time.sleep(2) # Sleep for 2 seconds
except KeyboardInterrupt:
    # Exit on CTRL-C
    pass 