import socket
import shutil
import psutil
from uptime import uptime
from datetime import date

hostName = socket.gethostname()

today = date.today()

total, used, free = shutil.disk_usage('D:\\')
percentFree = free * 100 /total
r_percentFree = round(percentFree)

ram = psutil.virtual_memory()
r_ramPercent = round(ram.percent)

daysUp= uptime()/60/60/24
r_daysUp = round(daysUp)

data=str(hostName)+'\t'+str(today)+'\t' +str(r_percentFree) +'\t'+ str(r_ramPercent) +'\t'+ str(r_daysUp)+'\n'

textfile= open("\\\\izenggs1\\Documentation Library\\Sistemas\\Checkbox\\data.txt", "a")
textfile.write(data)
textfile.close()

bat_file_path_28= r"C:\Users\Joel\Desktop\Developments\logs_generator\Workstations"
if r_daysUp >= 9:
    subprocess.run(bat_file_path_28)
