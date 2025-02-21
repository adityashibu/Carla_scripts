import carla
import time
import os
import cv2
import numpy as np

client = carla.Client("localhost", 2000)
client.set_timeout(10.0)
world = client.get_world()

bp_library = world.get_blueprint_library()
vehicle_bp = bp_library.find('vehicle.dodge.charger')

transform = world.get_map().get_spawn_points()[75]
vehicle = world.spawn_actor(vehicle_bp, transform)

def camFunc(data):
    i = np.array(data.raw_data)
    i2 = i.reshape((720, 1024, 4))
    i3 = i2[:, :, :3]
    
    cv2.imshow("", i3)
    cv2.waitKey(1)

rgb_cam = bp_library.find('sensor.camera.rgb')
rgb_cam.set_attribute("image_size_x", "1024")
rgb_cam.set_attribute("image_size_y", "720")
rgb_cam.set_attribute("fov", "90")

transform = carla.Transform(carla.Location(x=4,z=1.6),carla.Rotation(roll=0,pitch=0,yaw=0))
sensor = world.spawn_actor(rgb_cam, transform, attach_to=vehicle)

if not os.path.exists("output\\"):
    os.mkdir("output\\")
#sensor.listen(lambda data: data.save_to_disk('output/%.6d.jpg' % data.frame))
sensor.listen(lambda data: camFunc(data))

vehicle.set_autopilot(True)

time.sleep(60)
sensor.destroy()
vehicle.destroy()