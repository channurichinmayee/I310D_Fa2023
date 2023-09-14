import math

def calculate_volume_of_sphere(radius):
    volume = (4/3*(math.pi))*((radius)**3)
    return volume

radius_1 = 30
volume_1 = calculate_volume_of_sphere(radius_1)
print(volume_1)

radius_2 = 40
volume_2 = calculate_volume_of_sphere(radius_2)
print(volume_2)
