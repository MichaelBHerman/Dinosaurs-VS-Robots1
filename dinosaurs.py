
class Dinosaur:
    def __init__(self, name, attack_number, health_number):
        self.name = name
        self.attack_power = attack_number
        self.health = health_number

    def dino_attack(self, robot):
         robot.health_number -= (self.attack_power - robot.health)
