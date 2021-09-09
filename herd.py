from dinosaurs import Dinosaur

class Herd:
    def __init__(self):
        self.herd = []
        self.add_dinosaur_to_list()
    def add_dinosaur_to_list(self):
        dinosaur1 = Dinosaur("Raptor", 50, 120)
        dinosaur2 = Dinosaur("T-Rex", 100, 220)
        dinosaur3 = Dinosaur("Stegosaurus", 70, 300)

        self.herd.append(dinosaur1)
        self.herd.append(dinosaur2)
        self.herd.append(dinosaur3) 