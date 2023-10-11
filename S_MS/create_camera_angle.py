# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import math
import toml

Width = 352
Height = 128

img_width = [1600, 1600, 1600, 1600, 1600, 1600]
img_height = [900, 900, 900, 900, 900, 900]
# f = [1715.6055, 1715.6055, 1715.6055, 1715.6055, 1715.6055, 1715.6055] # camera narrow
f = [1142.53, 1142.53, 560.166, 1142.53, 1142.53, 1142.53] # camera wide

camera_yaw = [0, 55, 110, 180, 250, 305]


def main():

    Camera_angle_list = []
    for l in range(0, 6):
        u0 = img_width[l] / 2
        v0 = img_height[l] / 2
        list = []
        yw = camera_yaw[l]
        for w in range(0, Width - 1):
            for h in range(0, Height - 1):
                u = (w * img_width[l]) / Width
                v = (h * img_height[l]) / Height

                x = u - u0
                y = v - v0

                lyaw = math.sqrt(x * x + f[l] * f[l])
                lbeam = math.sqrt(x * x + y * y + f[l] * f[l])

                yaw = math.degrees(math.asin(x / lyaw)) + yw
                beam = math.degrees(math.asin(y / lbeam))

                c = []
                c.append(yaw)
                c.append(beam)
                list.append(c)

        Camera_angle_list.append(list)
        list = None

    data = open("multihyper_camera.toml", 'w')
    content = {
        'title': "Parameters",
        # pom
        'pom': {
        'pom_x': 60,
        'pom_y': 40,
        'pom_z': 4,
        'pom_exclude_x_min': 27,
        'pom_exclude_x_max': 33,
        'pom_exclude_y_min': 18,
        'pom_exclude_y_max': 22,
        'pom_exclude_z_min': 0,
        'pom_exclude_z_max': 4,
        'scale': 20},

        # lidar
        'lidar':{
        'x_min': 28,
        'x_max': 30.5,
        'y_min': 19,
        'y_max': 21,
        'z_min': 1.8,
        'z_max': 3,
        'yaw_min': "known",
        'yaw_max': "known",
        'pitch_min': -0.0001,
        'pitch_max': 0.0001,
        'roll_min': -0.0001,
        'roll_max': 0.0001,
        'beam_angle': [-25,-23,-21,-19,-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5],
        'lidar_nos': 6,
        'camera_angle': Camera_angle_list}
    }
    toml.dump(content, data)








if __name__ == "__main__":
    main()
    print('done.')