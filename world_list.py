import carla

client = carla.Client('localhost', 2000)
client.set_timeout(20.0)
world = client.get_world()

available_maps = client.get_available_maps()
print(available_maps)
