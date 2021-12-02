# Credits
This work is largely an adaptation from https://github.com/xingyizhou/CenterTrack showcasing the power of Grid and Pytorch Lightning Lite.

# Purpose
The purpose of this repository is to give reproducible steps to the following:
1. Deploy Center Track models locally
2. **Scale** Center Track model deployments with Grid
3. Automate Grid approach with git actions
4. **Optimize** model performance with Pytorch-lightning

# Prerequisites
To follow along exactly with this tutorial you will only need the following software:
1. Conda - https://docs.anaconda.com/anaconda/install/index.html
2. Python - https://www.python.org/downloads/

# Set Up Environment
The below commands can be used to set up the necessary environment. First we will set the variable CenterTrack_ROOT=/path/to/clone/CenterTrack. After doing that the code below should work for setting up the environment.

**For now you will manually have to convert from torch.hub import load_state_dict_from_url to from torchvision.models.utils import load_state_dict_from_url for this code to run. This change can be made in the /CenterTrack/src/lib/model/networks/backbones directory**

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
git clone https://github.com/oojo12/grid-center-track.git
cd grid-center-track
pip install -r requirements.txt
mv main-lite.py $CenterTrack_ROOT/src/
mv logger.py $CenterTrack_ROOT/src/lib
mv liteTrainer.py $CenterTrack_ROOT/src/lib
```

# Pytorch Example
1. Training on custom data section here https://github.com/xingyizhou/CenterTrack
2. Get example data - follow instructions at https://github.com/xingyizhou/CenterTrack/blob/master/readme/DATA.md
3. Run the below code.
```
cd $CenterTrack_ROOT/src
python main.py tracking --exp_id mot17_half_sc --dataset custom --custom_dataset_ann_path ../data/mot17/annotations/train_half.json --custom_dataset_img_path ../data/mot17/train/ --input_h 544 --input_w 960 --num_classes 1 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0,1
```

# Pytorch Lightning Example
1. Training on custom data section here https://github.com/xingyizhou/CenterTrack
2. Get example data - follow instructions at https://github.com/xingyizhou/CenterTrack/blob/master/readme/DATA.md
3. Run the below code
```
cd $CenterTrack_ROOT/src
python main-lite.py tracking --exp_id mot17_half_sc --dataset custom --custom_dataset_ann_path ../data/mot17/annotations/train_half.json --custom_dataset_img_path ../data/mot17/train/ --input_h 544 --input_w 960 --num_classes 1 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1
```

# Grid Multi-Node Example
TBD

