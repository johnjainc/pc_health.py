#!/usr/bin/env python3
import shutil
import psutil
#Function to check Disk usage
def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free

#Function to check CPU usage
def check_cpu_usage():
    usage=psutil.cpu_percent(0.1)
    return usage

if check_disk_usage("/")<50 and check_cpu_usage()<50:
    print("Everything is okay!")
else:
    print("ERROR!!!!")
