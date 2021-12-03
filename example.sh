# example running version to compare training speed of Pytorch vs Pytorch Lightning Lite. Modify the batch_size variable as needed.
python main.py tracking --exp_id mot17_fulltrain_sc --dataset mot --dataset_version 17trainval --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0 --batch_size=12
python main-lite.py tracking --exp_id mot17_fulltrain_sc --dataset mot --dataset_version 17trainval --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0 --batch_size=12
