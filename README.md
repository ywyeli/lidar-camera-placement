# Camera LiDAR Configuration for 3D Detection
This is the official code for ICRA 2024 "Influence of Camera-LiDAR Configuration on 3D Object Detection for Autonomous Driving". (https://arxiv.org/abs/2310.05245)


## Preparation
Download [CARLA v0.9.10](https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/CARLA_0.9.10.tar.gz) and unzip it under `./carla`. Follow the install instruction of `scenario_runner` of commit [ad71a2c](https://github.com/carla-simulator/scenario_runner/tree/ad71a2c7ed012d735be2b1158fca51b0761ff26b).

We test our repo with on Ubuntu 18.04 or 20.04.

## Data Collection

Turn on CARLA as default and then run the following shell script. 

`cd ./carla-nuscenes/scripts`

`bash routes_baselines.sh`

LiDAR configurations can be accessed at `./carla-nuscenes/hyperparams`. Camera configurations can be accessed in `./carla-nuscenes/scenario_runner/lidar.py`. The density of Vehicles and Pedestrians can be accessed on `Line 397-422` in `./carla-nuscenes/scenario_runner/srunner/scenarios/route_scenario.py`. The datasets can be accessed at `./carla-nuscenes/dataset`. 

Run the following code to create NuScenes-formatted labels.

`cp -r ./carla-nuscenes/dataset/[YOUR LIDAR PLACEMENT]/training/label_2 ./NuScenes_generate/label_2` 

`python ./NuScenes_generate/create_test_wide.py`

`python ./NuScenes_generate/create_trainval_wide.py`

Copy the folder `./NuScenes_generate/maps`, `./NuScenes_generate/v1.0-trainval` and `./NuScenes_generate/v1.0-test` to your dataset root. Replace the file `splits.py` in the NuScenes-devkit on your environment with our `./NuScenes_generate/splits.py`, otherwise the NuScenes-devkit can not recognize our dataset.

## Unified Surrogate Metric

The 3d bounding boxes of all 3d objects can be accessed at `./S_MS/routes`. Run the following code to calculate Unified Surrogate Metric (S-MS).

`python ./S_MS/create_camera_angle.py`

`python ./S_MS/evaluate_camera_position.py`

`python ./S_MS/evaluate_lidar_position.py`

### Reference
> - [Multi-LiDAR-Placement-for-3D-Detection](https://github.com/HanjiangHu/Multi-LiDAR-Placement-for-3D-Detection)
> - [CARLA v0.9.10](https://carla.readthedocs.io/en/0.9.10/)
> - [ScenarioRunner](https://github.com/carla-simulator/scenario_runner)
> - [NuScenes-devkit](https://github.com/nutonomy/nuscenes-devkit)
