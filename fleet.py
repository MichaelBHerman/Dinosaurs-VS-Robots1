from robots import Robot
from weapons import Weapon
import inspect

class Fleet:
    def __init__(self):
        self.fleet = []
        self.add_robots_to_fleet()
        
    
    def add_robots_to_fleet(self):
        weapon_one = Weapon("Tommy Gun", 65)
        weapon_two = Weapon("Katana", 40)
        weapon_three = Weapon("Rocket Launcher", 220) 

        robot1 = Robot("Wall-E", 55, weapon_three)
        robot2 = Robot("T-1000", 200, weapon_one)
        robot3 = Robot("Megazord", 300, weapon_two)

        self.fleet.append(robot1)
        self.fleet.append(robot2)
        self.fleet.append(robot3)

    def show_fleet(self):
        for robots in self.fleet():
            print(robots)
            # print(f"{self.fleet}") 