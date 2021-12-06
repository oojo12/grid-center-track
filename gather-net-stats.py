import time
import psutil
import subprocess

subprocess.run('echo "packets_sent, packets_received" > ../stats/net_stats.csv', shell=True)

while True:
    net_stats = psutil.net_io_counters()
    subprocess.run(f'echo "{net_stats.packets_sent}, {net_stats.packets_recv}" >> ../stats/net_stats.csv', shell=True)
    time.sleep(1)
