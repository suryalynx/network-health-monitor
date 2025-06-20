import datetime
import csv
import os
import psutil
import platform
import subprocess

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().available // 1024
try:
    disk = psutil.disk_usage('C:\\').free
except:
    disk = psutil.disk_usage('/').free
ping_status = ping("google.com")
av_status = "Unknown"  # Optional: Extend with AV check using WMI

log_data = [now, ping_status, cpu, ram, disk, av_status]

filename = f"{log_dir}/log-{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
with open(filename, mode='a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(log_data)