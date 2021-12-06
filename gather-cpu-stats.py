import csv
import time
import psutil
import subprocess


p = psutil.Process()
with p.oneshot():
    p.name()  # execute internal routine once collecting multiple info
    p.memory_percent()  # return cached value
    p.cpu_percent()  # return cached value

subprocess.run('echo "per_cpu_utilization, per_ram_utilization" > ../stats/cpu_stats.csv', shell=True)

while True:
    subprocess.run(f'echo "{p.memory_percent()}, {p.cpu_percent()}" >> ../stats/cpu_stats.csv', shell=True)
    time.sleep(1)
