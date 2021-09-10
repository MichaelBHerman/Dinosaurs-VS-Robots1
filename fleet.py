from robots import Robot
from weapons import Weapon

# weapon_one = Weapon("Tommy Gun", 65)
# weapon_two = Weapon("Katana", 40)
# weapon_three = Weapon("Rocket Launcher", 220)

class Fleet:
    def __init__(self):
          
        self.fleet_list = [(Robot("Wall-E", 55, 65)),
                          (Robot("T-1000", 200, 40)),
                          (Robot("Megazord", 300, 220))]
        
        
        
    
    
        

        
    def show_fleet(self):
        for robots in self.fleet:
            print(robots.name)
            # print(f"{self.fleet}") 