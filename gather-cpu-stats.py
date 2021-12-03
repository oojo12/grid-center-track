import csv
import time
import psutil
p = psutil.Process()
with p.oneshot():
    p.name()  # execute internal routine once collecting multiple info
    p.memory_percent()  # return cached value
    p.cpu_percent()  # return cached value

with open('../stats/cpu_stats.csv', 'w', newline='') as csvfile:
    fields = ['per_cpu_utilization', 'per_ram_utilization']
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fields)
    while True:
        writer.writerow([p.memory_percent(), p.cpu_percent()])
        time.sleep(1)
