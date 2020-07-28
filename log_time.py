import os

import time
from datetime import datetime

now = datetime.now()
# Main loop to print the temperature every second.
dt_string = now.strftime("%d%m%Y_%H%M%S")

file_Data = open("timelog_" + dt_string + ".txt" , "w" )

for i in range 20:
	# Read temperature.
	#temp = sensor.temperature
	# Print the value.
	dt_string = now.strftime("%d%m%Y_%H%M%S")

	print("Time: ", (dt_string))
	# Delay for a second.
	time.sleep(1.0)
	#print("file design closed")
	file_Data.write(str(dt_string))
	file_Data.write("\n")

file_Data.close()
