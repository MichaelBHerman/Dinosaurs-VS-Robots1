from dinosaurs import Dinosaur
import inspect

player_one = Dinosaur("Raptor", 50, 120)
player_two = Dinosaur("T-Rex", 100, 220)
player_three = Dinosaur("Stegosaurus", 70, 300)

from weapons import Weapon

weapon_one = Weapon("Tommy Gun", 65)
weapon_two = Weapon("Katana", 40)
weapon_three = Weapon("Rocket Launcher", 220)

from robots import Robot

robot_one = Robot("Wall-E", 55, weapon_three)
robot_two = Robot("T-1000", 200, weapon_one)
robot_three = Robot("Megazord", 300, weapon_two)

from fleet import Fleet
robot_fleet = Fleet()
robot_fleet.add_robots_to_fleet
print(Fleet)

from herd import Herd
dinosaur_herd = Herd()

