# Credits
This work is largely an adaptation from https://github.com/xingyizhou/CenterTrack showcasing the power of Grid and Pytorch Lightning Lite.

# Purpose
The purpose of this repository is to give reproducible steps to the following:
1. Deploy Center Track models locally
2. **Scale** Center Track model deployments with Grid
3. Automate Grid approach with git actions
4. **Simplify** model code with Pytorch-lightning

# Prerequisites
To follow along exactly with this tutorial you will need the following software:
1. Conda - https://docs.anaconda.com/anaconda/install/index.html
2. Python - https://www.python.org/downloads/
3. Nvidia-smi
4. Git
5. nohup

# Set Up Software Environment
The below commands can be used to set up the necessary environment. First we will set the variable CenterTrack_ROOT=/path/to/clone/CenterTrack. After doing that the code below should work for setting up the environment.

```
# Grid.ai Virtual Environment. These are modified from the steps at https://github.com/xingyizhou/CenterTrack/blob/master/readme/INSTALL.md

conda create --name CenterTrack python=3.6 -y
conda activate CenterTrack
conda install pytorch=1.9.1 torchvision=0.10.0 -c pytorch -y
pip install lightning-grid --upgrade; pip install -U "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
git clone --recursive https://github.com/xingyizhou/CenterTrack $CenterTrack_ROOT
cd $CenterTrack_ROOT/src/lib/model/networks/
git clone https://github.com/lbin/DCNv2.git
cd DCNv2
git checkout remotes/origin/pytorch_1.9
./make.sh
cd $CenterTrack_ROOT
mkdir data
mkdir stats
git clone https://github.com/oojo12/grid-center-track.git
cd grid-center-track
pip install -r requirements.txt
mv main-lite.py $CenterTrack_ROOT/src/
mv logger.py $CenterTrack_ROOT/src/lib
mv liteTrainer.py $CenterTrack_ROOT/src/lib
mv gather-stats.sh  $CenterTrack_ROOT/src/
mv gather-cpu-stats.py $CenterTrack_ROOT/src/
mv gather-net-stats.py $CenterTrack_ROOT/src/
mv get_mot_17.sh $CenterTrack_ROOT/src/tools/
```

# Pytorch Example
```
cd $CenterTrack_ROOT/src/tools/
bash get_mot_17.sh
python main.py tracking --exp_id mot17_half_sc --dataset custom --custom_dataset_ann_path ../data/mot17/annotations/train_half.json --custom_dataset_img_path ../data/mot17/train/ --input_h 544 --input_w 960 --num_classes 1 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0,1
```

# Pytorch Lightning Example
```
cd $CenterTrack_ROOT/src/tools/
bash get_mot_17.sh
python main-lite.py tracking --exp_id mot17_half_sc --dataset custom --custom_dataset_ann_path ../data/mot17/annotations/train_half.json --custom_dataset_img_path ../data/mot17/train/ --input_h 544 --input_w 960 --num_classes 1 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1
```
# Grid
## Set Up w/ Grid CLI
1. install grid - pip install lightning-grid --upgrade
2. log into grid - grid login #you will be prompted to log in with your api key and username. Alternatively you can visit https://platform.grid.ai/#/settings?tabId=apikey and the exact command will be given to you
3. If you logged in with Google you may want to visit https://platform.grid.ai/#/settings?tabId=integrations and integrate your Grid account with your Github if you plan on using public or private repos with grid run. Alternatively you can use the localdir flag for local directories
4. Visit "Step 4: Start a Session" https://docs.grid.ai/start-here/typical-workflow-cli-user 
5. Visit session via ssh or UI. Instructions here (https://docs.grid.ai/start-here/typical-workflow-cli-user  step 5)
6. Run code in "Set Up Software Environment" Section

## Set up Grid UI
The steps are very similar to the above and the reader is advised to visit https://docs.grid.ai/start-here/typical-workflow-web-user for complete instructions.

## Grid Multi-Node Example
TO DO

# Statistics
## Gathering
The below code will collect the below statistics as background processes. To kill the background process run ps to find the process id and follow up with a kill command.
1. GPU utlization and GPU RAM utilization
2. CPU utilization and RAM utilization
3. Network bandwidth and network packets - TO DO
4. Storage iops and storage bandwidth - TO DO

```
cd $CenterTrack_ROOT/src
gather-stats.sh
```
