# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import json
from math import pi, sin, cos


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# open label folder
def openreadtxt(file_name):
    data = []
    file = open(file_name, 'r')
    file_data = file.readlines()
    for row in file_data:
        tmp_list = row.split(' ')
        data.append(tmp_list)
    return data


def create_sensor_json(sensor_json, sensor_list):
    create_sensor_token = None
    for s in sensor_list:
        if s == 'LIDAR_TOP':
            modality = 'lidar'
            create_sensor_token = 'lidartoplidartoplidartoplidartop'
        else:
            modality = 'camera'
            if s == 'CAM_FRONT':
                create_sensor_token = 'camfrontcamfrontcamfrontcamfront'
            if s == 'CAM_BACK':
                create_sensor_token = 'cambackcambackcambackcambackcamb'
            if s == 'CAM_FRONT_LEFT':
                create_sensor_token = 'camfrontleftcamfrontleftcamfront'
            if s == 'CAM_FRONT_RIGHT':
                create_sensor_token = 'camfrontrightcamfrontrightcamfro'
            if s == 'CAM_BACK_LEFT':
                create_sensor_token = 'cambackleftcambackleftcambacklef'
            if s == 'CAM_BACK_RIGHT':
                create_sensor_token = 'cambackrightcambackrightcambackr'
        sensor_json.append(
            {'token': create_sensor_token,
             'channel': s,
             'modality': modality}
        )
    sensor_jsondata = json.dumps(sensor_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/sensor.json', 'w')
    f.write(sensor_jsondata)
    f.close()


def create_visibility_json(visibility_json):
    visibility_json.append(
        {'description': 'visibility of whole object is between 80 and 100%',
         'token': '4',
         'level': 'v80-100'}
    )
    visibility_json.append(
        {'description': 'visibility of whole object is between 60 and 80%',
         'token': '3',
         'level': 'v60-80'}
    )
    visibility_json.append(
        {'description': 'visibility of whole object is between 40 and 60%',
         'token': '2',
         'level': 'v40-60'}
    )
    visibility_json.append(
        {'description': 'visibility of whole object is between 20 and 40%',
         'token': '1',
         'level': 'v20-40'}
    )
    visibility_jsondata = json.dumps(visibility_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/visibility.json', 'w')
    f.write(visibility_jsondata)
    f.close()


def create_category_json(category_json):
    create_category_token = 'vehiclecarvehiclecarvehiclecarve'
    category_json.append(
        {'token': create_category_token,
         'name': 'vehicle.car',
         'description': 'vehicle_car'}
    )
    create_category_token = 'humanpedestrianadulthumanpedestr'
    category_json.append(
        {'token': create_category_token,
         'name': 'human.pedestrian.adult',
         'description': 'human_pedestrian_adult'}
    )
    create_category_token = 'vehiclebicyclevehiclebicyclevehi'
    category_json.append(
        {'token': create_category_token,
         'name': 'vehicle.bicycle',
         'description': 'vehicle_bicycle'}
    )
    category_jsondata = json.dumps(category_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/category.json', 'w')
    f.write(category_jsondata)
    f.close()


def create_attribute_json(attribute_json):
    create_attribute_token = 'vehiclemovingvehiclemovingvehicl'
    attribute_json.append(
        {'token': create_attribute_token,
         'name': 'vehicle.moving',
         'description': 'vehicle_moving'}
    )
    create_attribute_token = 'pedestrianmovingpedestrianmoving'
    attribute_json.append(
        {'token': create_attribute_token,
         'name': 'pedestrian.moving',
         'description': 'pedestrian_moving'}
    )
    create_attribute_token = 'cyclewithridercyclewithridercycl'
    attribute_json.append(
        {'token': create_attribute_token,
         'name': 'cycle.with_rider',
         'description': 'cycle_with_rider'}
    )
    attribute_jsondata = json.dumps(attribute_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/attribute.json', 'w')
    f.write(attribute_jsondata)
    f.close()


def create_log_json(log_json):
    log_json.append(
        {'token': 'logtokenlogtokenlogtokenlogtoken',
         'logfile': 'n008-2018-08-01-00-00-00-0400',
         'vehicle': 'n008',
         'date_captured': '2018-08-01',
         'location': 'carla'}
    )
    log_jsondata = json.dumps(log_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/log.json', 'w')
    f.write(log_jsondata)
    f.close()


def create_map_json(map_json):
    map_json.append({
        "category": "semantic_prior",
        "token": "53992ee3023e5494b90c316c183be829",
        "filename": "maps/53992ee3023e5494b90c316c183be829.png",
        "log_tokens": [
        "logtokenlogtokenlogtokenlogtoken"
        ]
    })
    map_jsondata = json.dumps(map_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/map.json', 'w')
    f.write(map_jsondata)
    f.close()


def create_calibrated_sensor_json(calibrated_sensor_json, sensor_list):
    create_sensor_token = None
    create_calibrated_sensor_token = None
    for s in sensor_list:
        if s == 'LIDAR_TOP':
            create_sensor_token = 'lidartoplidartoplidartoplidartop'
            create_calibrated_sensor_token = '90000000000000000000000000000000'
            translation = [0, 0, 1.8]
            rotation = [
                0.707, 0, 0, -0.707
            ]
            camera_intrinsic = []
        if s == 'CAM_FRONT':
            create_sensor_token = 'camfrontcamfrontcamfrontcamfront'
            create_calibrated_sensor_token = '90000000000000000000000000000001'
            translation = [0.5, 0, 1.8]
            rotation = [
                0.5, -0.5, 0.5, -0.5
            ]
            camera_intrinsic = [
                [1142.53, 0.0, 800],
                [0.0, 1142.53, 450],
                [0.0, 0.0, 1.0]
            ]
        if s == 'CAM_BACK':
            create_sensor_token = 'cambackcambackcambackcambackcamb'
            create_calibrated_sensor_token = '90000000000000000000000000000002'
            translation = [-1.5, 0, 1.8]
            rotation = [
                0.5, -0.5, -0.5, 0.5
            ]
            camera_intrinsic = [
                [560.166, 0.0, 800],
                [0.0, 560.166, 450],
                [0.0, 0.0, 1.0]
            ]
        if s == 'CAM_FRONT_LEFT':
            create_sensor_token = 'camfrontleftcamfrontleftcamfront'
            create_calibrated_sensor_token = '90000000000000000000000000000003'
            translation = [0.5, 0.5, 1.8]
            rotation = [
                0.674,
                -0.674,
                0.213,
                -0.213
            ]
            camera_intrinsic = [
                [1142.53, 0.0, 800],
                [0.0, 1142.53, 450],
                [0.0, 0.0, 1.0]
            ]
        if s == 'CAM_FRONT_RIGHT':
            create_sensor_token = 'camfrontrightcamfrontrightcamfro'
            create_calibrated_sensor_token = '90000000000000000000000000000004'
            translation = [0.5, -0.5, 1.8]
            rotation = [
                0.213,
                -0.213,
                0.674,
                -0.674
            ]
            camera_intrinsic = [
                [1142.53, 0.0, 800],
                [0.0, 1142.53, 450],
                [0.0, 0.0, 1.0]
            ]
        if s == 'CAM_BACK_LEFT':
            create_sensor_token = 'cambackleftcambackleftcambacklef'
            create_calibrated_sensor_token = '90000000000000000000000000000005'
            translation = [-1.0, 0.5, 1.8]
            rotation = [
                0.696,
                -0.696,
                -0.123,
                0.123
            ]
            camera_intrinsic = [
                [1142.53, 0.0, 800],
                [0.0, 1142.53, 450],
                [0.0, 0.0, 1.0]
            ]
        if s == 'CAM_BACK_RIGHT':
            create_sensor_token = 'cambackrightcambackrightcambackr'
            create_calibrated_sensor_token = '90000000000000000000000000000006'
            translation = [-1.0, -0.5, 1.8]
            rotation = [
                0.123,
                -0.123,
                -0.696,
                0.696
            ]
            camera_intrinsic = [
                [1142.53, 0.0, 800],
                [0.0, 1142.53, 450],
                [0.0, 0.0, 1.0]
            ]

        calibrated_sensor_json.append(
            {'token': create_calibrated_sensor_token,
             'sensor_token': create_sensor_token,
             'translation': translation,
             'rotation': rotation,
             'camera_intrinsic': camera_intrinsic}
        )
    calibrated_sensor_jsondata = json.dumps(calibrated_sensor_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/calibrated_sensor.json', 'w')
    f.write(calibrated_sensor_jsondata)
    f.close()


# write json file
def nuread(pathh):
    files = os.listdir(pathh)
    scene_json = []
    sensor_json = []
    calibrated_sensor_json = []
    log_json = []
    sample_json = []
    sample_annotation_json = []
    sample_data_json = []
    instance_json = []
    ego_pose_json = []
    attribute_json = []
    category_json = []
    visibility_json = []
    map_json = []

    sensor_list = ['LIDAR_TOP', 'CAM_BACK', 'CAM_BACK_LEFT', 'CAM_BACK_RIGHT',
                   'CAM_FRONT', 'CAM_FRONT_LEFT', 'CAM_FRONT_RIGHT']

    # timestamp
    timestamp = 0

    # calibrated_sensor_token
    calibrated_sensor_token = 0

    # scene_name
    scene_name = 7001

    # scene_token
    scene_token = 77000000000000000000000000000001

    # sample_token
    sample_token = 17000000000000000000000000000001

    # sample_annotation_token
    sample_annotation_token = 27000000000000000000000000000001

    # ego_pose_token
    ego_pose_token = 0

    # sample_data_token
    sample_data_token_lidar_top = 37000000000000000000000000000001

    sample_data_token_cam_front = 37100000000000000000000000000001

    sample_data_token_cam_back = 37200000000000000000000000000001

    sample_data_token_cam_front_left = 37300000000000000000000000000001

    sample_data_token_cam_front_right = 37400000000000000000000000000001

    sample_data_token_cam_back_left = 37500000000000000000000000000001

    sample_data_token_cam_back_right = 37600000000000000000000000000001


    # instance_token
    instance_token = 47000000000000000000000000000001

    category_token = None

    attribute_tokens = None

    # open txt file
    for i in range(1, 40000):
        file_no = 1500000000000000 + i

        f = str(file_no)
        if f[-3] == '0':

            # timestamp
            print('--- New task ---')
            print('Past:', timestamp)
            # timestamp = file.split('.')[0]
            timestamp = str(file_no)
            print('Next:', timestamp)

            # open position
            # position = pathh + '/' + file
            position = pathh + '/' + str(file_no) + '.txt'

            if os.path.exists(position):
                datas = openreadtxt(position)
            else:
                continue
            print('Generating...')

            if sample_token % 40 == 1:
                sample_json.append(
                    {'token': str(sample_token),
                     'timestamp': int(timestamp),
                     'prev': '',
                     'next': str(sample_token + 1),
                     'scene_token': str(scene_token)}
                )
            elif sample_token % 40 == 0:
                sample_json.append(
                    {'token': str(sample_token),
                     'timestamp': int(timestamp),
                     'prev': str(sample_token - 1),
                     'next': '',
                     'scene_token': str(scene_token)}
                )
            else:
                sample_json.append(
                    {'token': str(sample_token),
                     'timestamp': int(timestamp),
                     'prev': str(sample_token - 1),
                     'next': str(sample_token + 1),
                     'scene_token': str(scene_token)}
                )

            for s in sensor_list:
                if s == 'LIDAR_TOP':
                    fileformat = 'pcd'
                    forma = '.pcd.bin'
                    height = 0
                    width = 0
                    calibrated_sensor_token = '90000000000000000000000000000000'
                    ego_pose_token = sample_data_token_lidar_top
                else:
                    fileformat = 'jpg'
                    forma = '.jpg'
                    height = 900
                    width = 1600
                    if s == 'CAM_FRONT':
                        calibrated_sensor_token = '90000000000000000000000000000001'
                        ego_pose_token = sample_data_token_cam_front
                    if s == 'CAM_BACK':
                        calibrated_sensor_token = '90000000000000000000000000000002'
                        ego_pose_token = sample_data_token_cam_back
                    if s == 'CAM_FRONT_LEFT':
                        calibrated_sensor_token = '90000000000000000000000000000003'
                        ego_pose_token = sample_data_token_cam_front_left
                    if s == 'CAM_FRONT_RIGHT':
                        calibrated_sensor_token = '90000000000000000000000000000004'
                        ego_pose_token = sample_data_token_cam_front_right
                    if s == 'CAM_BACK_LEFT':
                        calibrated_sensor_token = '90000000000000000000000000000005'
                        ego_pose_token = sample_data_token_cam_back_left
                    if s == 'CAM_BACK_RIGHT':
                        calibrated_sensor_token = '90000000000000000000000000000006'
                        ego_pose_token = sample_data_token_cam_back_right

                filename = 'samples/' + s + '/n008-2018-08-01-00-00-00-0400__' + s + '__' + timestamp + forma

                if sample_token % 40 == 1:
                    sample_data_json.append(
                        {'token': str(ego_pose_token),
                         'sample_token': str(sample_token),
                         'ego_pose_token': str(ego_pose_token),
                         'calibrated_sensor_token': calibrated_sensor_token,
                         'timestamp': int(timestamp),
                         'fileformat': fileformat,
                         'is_key_frame': True,
                         'height': height,
                         'width': width,
                         'filename': filename,
                         'prev': '',
                         'next': str(ego_pose_token + 1)}
                    )
                elif sample_token % 40 == 0:
                    sample_data_json.append(
                        {'token': str(ego_pose_token),
                         'sample_token': str(sample_token),
                         'ego_pose_token': str(ego_pose_token),
                         'calibrated_sensor_token': calibrated_sensor_token,
                         'timestamp': int(timestamp),
                         'fileformat': fileformat,
                         'is_key_frame': True,
                         'height': height,
                         'width': width,
                         'filename': filename,
                         'prev': str(ego_pose_token - 1),
                         'next': ''}
                    )
                else:
                    sample_data_json.append(
                        {'token': str(ego_pose_token),
                         'sample_token': str(sample_token),
                         'ego_pose_token': str(ego_pose_token),
                         'calibrated_sensor_token': calibrated_sensor_token,
                         'timestamp': int(timestamp),
                         'fileformat': fileformat,
                         'is_key_frame': True,
                         'height': height,
                         'width': width,
                         'filename': filename,
                         'prev': str(ego_pose_token - 1),
                         'next': str(ego_pose_token + 1)}
                    )

                ego_pose_json.append(
                    {'token': str(ego_pose_token),
                     'timestamp': int(timestamp),
                     'rotation': [1, 0, 0, 0],
                     'translation': [0, 0, 0]}
                )

            # next sample_data_token
            sample_data_token_lidar_top = sample_data_token_lidar_top + 1
            sample_data_token_cam_front = sample_data_token_cam_front + 1
            sample_data_token_cam_back = sample_data_token_cam_back + 1
            sample_data_token_cam_front_left = sample_data_token_cam_front_left + 1
            sample_data_token_cam_front_right = sample_data_token_cam_front_right + 1
            sample_data_token_cam_back_left = sample_data_token_cam_back_left + 1
            sample_data_token_cam_back_right = sample_data_token_cam_back_right + 1

            for data in datas:
                if data[0] == 'Car':
                    category_token = 'vehiclecarvehiclecarvehiclecarve'
                    attribute_tokens = 'vehiclemovingvehiclemovingvehicl'
                    print(data)
                if data[0] == 'Pedestrian':
                    category_token = 'humanpedestrianadulthumanpedestr'
                    attribute_tokens = 'pedestrianmovingpedestrianmoving'
                    print(data)
                if data[0] == 'Cyclist':
                    category_token = 'vehiclebicyclevehiclebicyclevehi'
                    attribute_tokens = 'cyclewithridercyclewithridercycl'
                    print(data)

                rotation1 = [cos((- float(data[14]) - pi / 2) / 2), 0, 0, sin((- float(data[14]) - pi / 2) / 2)]

                sample_annotation_json.append({
                    'token': str(sample_annotation_token),
                    'sample_token': str(sample_token),
                    'instance_token': str(instance_token),
                    'visibility_token': '4',
                    'attribute_tokens': [
                        attribute_tokens
                        ],
                    'translation': [float(data[13]), - float(data[11]), float(data[8]) / 2],  #
                    'size': [float(data[9]), float(data[10]), float(data[8])],
                    'rotation': rotation1,
                    'prev': '',
                    'next': '',
                    'num_lidar_pts': 10,
                    'num_radar_pts': 0
                })

                # else:
                #     sample_annotation_json.append({
                #         'token': str(sample_annotation_token),
                #         'sample_token': str(sample_token),
                #         'instance_token': str(instance_token),
                #         'visibility_token': '4',
                #         'attribute_tokens': attribute_tokens,
                #         'translation': [float(data[13]), - float(data[11]), float(data[8]) / 2],  #
                #         'size': [float(data[9]), float(data[10]), float(data[8])],
                #         'rotation': rotation1,
                #         'prev': str(sample_annotation_token - 1),
                #         'next': str(sample_annotation_token + 1),
                #         'num_lidar_pts': 10,
                #         'num_radar_pts': 0
                #     })

                instance_json.append(
                    {'token': str(instance_token),
                     'category_token': category_token,
                     'nbr_annotations': 1,
                     'first_annotation_token': str(sample_annotation_token),
                     'last_annotation_token': str(sample_annotation_token)}
                )

                sample_annotation_token = sample_annotation_token + 1
                instance_token = instance_token + 1

            if sample_token % 40 == 0:
                name = 'carla-' + str(scene_name)
                scene_json.append(
                    {'token': str(scene_token),
                     'log_token': 'logtokenlogtokenlogtokenlogtoken',
                     'nbr_samples': 40,
                     'first_sample_token': str(sample_token - 39),
                     'last_sample_token': str(sample_token),
                     'name': name,
                     'description': 'carla'}
                )
                scene_token = scene_token + 1
                scene_name = scene_name + 1

            # next sample
            sample_token = sample_token + 1

        # scene_json.append(
        #     {'token': 'scenetoken0scenetoken0scenetoken',
        #      'log_token': 'logtokenlogtokenlogtokenlogtoken',
        #      'nbr_samples': sample_token - 10000000000000000000000000000000,
        #      'first_sample_token': str(10000000000000000000000000000001),
        #      'last_sample_token': str(sample_token),
        #      'name': 'carla-0001',
        #      'description': 'carla'}
        # )

    name = 'carla-' + str(scene_name)
    scene_json.append(
        {'token': str(scene_token),
         'log_token': 'logtokenlogtokenlogtokenlogtoken',
         'nbr_samples': (sample_token - 1) % 40,
         'first_sample_token': str(sample_token - 1 - ((sample_token - 1) % 40) + 1),
         'last_sample_token': str(sample_token - 1),
         'name': name,
         'description': 'carla'}
    )

    scene_jsondata = json.dumps(scene_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/scene.json', 'w')
    f.write(scene_jsondata)
    f.close()

    sample_jsondata = json.dumps(sample_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/sample.json', 'w')
    f.write(sample_jsondata)
    f.close()

    sample_annotation_jsondata = json.dumps(sample_annotation_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/sample_annotation.json', 'w')
    f.write(sample_annotation_jsondata)
    f.close()

    instance_jsondata = json.dumps(instance_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/instance.json', 'w')
    f.write(instance_jsondata)
    f.close()

    sample_data_jsondata = json.dumps(sample_data_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/sample_data.json', 'w')
    f.write(sample_data_jsondata)
    f.close()

    ego_pose_jsondata = json.dumps(ego_pose_json, indent=4, separators=(',', ':'))
    f = open('v1.0-test/ego_pose.json', 'w')
    f.write(ego_pose_jsondata)
    f.close()

    create_sensor_json(sensor_json, sensor_list)
    create_calibrated_sensor_json(calibrated_sensor_json, sensor_list)
    create_category_json(category_json)
    create_visibility_json(visibility_json)
    create_attribute_json(attribute_json)
    create_log_json(log_json)
    create_map_json(map_json)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.makedirs("v1.0-test", exist_ok=True)
    pat = "./label_2"
    nuread(pat)
    print_hi('Ye Li')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
