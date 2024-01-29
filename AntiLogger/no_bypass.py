import os, time
default_time=time.time()

while True: 
    if (time.time()-default_time)>=120: 
        os.system('shutdown /s')
    Tasks = os.popen('TASKLIST /FI  "IMAGENAME eq Taskmgr.exe"').read()
    if "PID" in Tasks:
        os.system("TASKKILL /F /IM Taskmgr.exe")
    LogsLogger= os.popen('TASKLIST /FI "WINDOWTITLE eq LogsLogger"').read()
    if "PID" in LogsLogger:
        print("Logs logger active")
    else:
        LogsLoggerSuccess=os.popen('TASKLIST /FI "WINDOWTITLE eq LogsLoggerSuccess"').read()
        if "PID" in LogsLoggerSuccess:
            exit()
        print("Inactive")
        os.system('shutdown /s')

#  os.system("start python C:/Users/antoinecarsenat/Desktop/AntiLogger/main.py")
