import socket
import shutil
import psutil
import datetime	#modulo para fechas
import subprocess
import re


from uptime import uptime
from datetime import date

hora_ejecucion = datetime.datetime.now()

hostName = socket.gethostname()

today = date.today()

total, used, free = shutil.disk_usage('C:\\')
percentFree = free * 100 /total
r_percentFree = round(percentFree)

ram = psutil.virtual_memory()
r_ramPercent = round(ram.percent)

daysUp= uptime()/60/60/24
r_daysUp = round(daysUp)


command_chassis= "omreport chassis | findstr Critical"
command_vdisk= "omreport storage vdisk | findstr Critical"
command_controller= "omreport storage controller | findstr Critical"
command_enclosure= "omreport storage enclosure | findstr Critical"
command_battery= "omreport storage battery | findstr Critical"

all_commands=[command_chassis,command_vdisk,command_controller,command_enclosure,command_battery]

txt_all=[]

for i in all_commands:
	txt=subprocess.getoutput(i)
	txt_re=re.findall("Critical|Non-Critical",txt)
	#txt_re.append("prueba")
	print(txt_re)
	#if len(txt_re)>0:
	#	txt_all.append(txt_re[0])
	for i in range(0,len(txt_re)): txt_all.append(txt_re[i])


if "Critical" in txt_all:
	Status="Critical"
elif "Non-Critical" in txt_all:
	Status="Non-Critical"
else:
	Status="Ok"


data=str(hostName)+'\t'+str(today)+'\t' +str(r_percentFree) +'\t'+ str(r_ramPercent) +'\t'+ str(r_daysUp) +'\t'+ str(hora_ejecucion)+'\t'+ str(Status) +'\n'

textfile= open("\\\\izenggs1\\Documentation Library\\Sistemas\\Checkbox\\data.txt", "a")
textfile.write(data)
textfile.close()