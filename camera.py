import carla
import math
import random 
import time 
import numpy as np
# import cv2

client = carla.Client('localhost', 2000)
world = client.get_world()

bp_lib = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()

# for bp in bp_lib.filter('vehicle'):
#     print(bp.id)

vehicle_bp = bp_lib.find('vehicle.dodge.charger')
vehicle = world.spawn_actor(vehicle_bp, random.choice(spawn_points))


spectator = world.get_spectator()
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4, z=2.5)), vehicle.get_transform().rotation)
spectator.set_transform(transform)

camera_bp = bp_lib