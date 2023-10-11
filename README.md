# Camera-LiDAR-Placement-for-3D-Detection
This is the official code for investigating the impact of Camera-LiDAR placement on object detection for autonomous driving.


## Preparation
Download [CARLA v0.9.10](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.tar.gz) and unzip it under `./carla`. Follow the install instruction of `scenario_runner` of commit [ad71a2c](https://github.com/carla-simulator/scenario_runner/tree/ad71a2c7ed012d735be2b1158fca51b0761ff26b).

We test our repo with on Ubuntu 18.04 or 20.04.



## Data Collection

Turn on CARLA as default and then run the following shell script. 

`cd ./carla-nuscenes/scripts`

`bash routes_baselines.sh`

Different LiDAR configurations can be accessed at `./carla-nuscenes/hyperparams`. Different Camera configurations can be modified at `./carla-nuscenes/scenario_runner/lidar.py`. The density of Vehicles and Pedestrians can be changed on `Line 397-422` in `./carla-nuscenes/scenario_runner/srunner/scenarios/route_scenario.py`.

The datasets can be accessed at `./carla-nuscenes/dataset`. Before training, run the following code to create NuScenes-formatted labels.

`cp -r ./carla-nuscenes/dataset/LIDAR PLACEMENT/training/label_2 ./createmeta/label_2` 
(e.g. `cp -r ./carla-nuscenes/dataset/center/training/label_2 ./createmeta/label_2`)

`cd ./createmeta`

`python create_trainval.py`

`python create_test.py`

Copy the folder `v1.0-trainval` and `v1.0-test` to your dataset root.



### Reference
> - [Multi-LiDAR-Placement-for-3D-Detection](https://github.com/HanjiangHu/Multi-LiDAR-Placement-for-3D-Detection)
> - [CARLA v0.9.10](https://carla.readthedocs.io/en/0.9.10/)
> - [ScenarioRunner](https://github.com/carla-simulator/scenario_runner)
> - [OpenPCDet](https://github.com/open-mmlab/OpenPCDet) of commit [`cbf2f4e`](https://github.com/open-mmlab/OpenPCDet/tree/cbf2f4eb0996c939017877b4c0713b2bb144a54e)
