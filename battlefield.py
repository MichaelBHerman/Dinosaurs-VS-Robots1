from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.welcome = self.dipslay_welcome()

# def show_fleet(self):
#     for robots in self.fleet:
#         print(f"{self.fleet.name}")

    def display_welcome(self):
        print("Welcome to the Battlefield!  Where Dinos and Robots come to duel for supremacy!")
        player_one = input("Choose your allegiance: Type Dinosaurs or Robots: ".lower())

    def battle(self):
        
        dinos=0
        robos=0
        while robos <=2 or dinos <=2:
            print("The dinosaurs prepare for attack.")
            self.herd.herd_list[dinos].dino_attack(self.fleet.fleet_list[robos])
            
            print(self.fleet.fleet_list[robos].health)
            
            if self.fleet.fleet_list[robos].health_number <= 0:
                print("A robot has been eliminated!")
            
                robos += 1
            if robos == 3 and self.fleet.fleet_list[2].health_number <= 0:
                print("The Dinosaurs have emerged victorious!")
                break
            
            print("The robot furociously attacks the dino!.")
            self.fleet.fleet_list[robos].robot_attack(self.herd.herd_list[dinos])
            
            if self.herd.herd_list[dinos].health_number <= 0:
                print("A dinosaur has been eliminated!")
                dinos +=1
            if dinos == 3 and self.herd.herd_list[2].health_number <= 0:
                print("The Robots are declared the victors!")
                break
