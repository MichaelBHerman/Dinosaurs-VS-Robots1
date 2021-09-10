from weapons import Weapon


class Robot:
    def __init__(self, name, attack_number, health_number):
        self.name = name
        self.health = health_number
        self.attack_power = attack_number
    
    def robot_attack(self, dinosaur): 
        dinosaur.health_number -= (self.attack_power - dinosaur.health)

       