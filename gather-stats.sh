#bin/bash
nohup nvidia-smi --query-gpu=utilization.gpu --format=csv --loop=1 >> ../stats/gpu_compute_utilization.txt &
nohup nvidia-smi --query-gpu=utilization.memory --format=csv --loop=1 >> ../stats/gpu_memory_utilization.txt &
python gather-cpu-stats.py
