#bin/bash
nohup nvidia-smi --query-gpu=utilization.gpu --format=csv --loop=1 >> ../stats/gpu_compute_utilization.txt &
nohup nvidia-smi --query-gpu=utilization.memory --format=csv --loop=1 >> ../stats/gpu_memory_utilization.txt &
nohup python gather-cpu-stats.py > /dev/null 2>&1 & 
nohup python gather-net-stats.py > /dev/null 2>&1 & 
