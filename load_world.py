import carla

client = carla.Client('localhost', 2000)
client.set_timeout(20.0)

client.load_world("Town10HD_Opt")
