from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet.fleet

def show_fleet(self):
    for robots in self.fleet.fleet:
        print(f"{self.fleet.type}")




print("Welcome to the Battlefield!  Where Dinos and Robots come to duel for supremacy")
player_one = input("Choose your allegiance: Type Dinosaurs or Robots: ".lower())

def play(chars):
    print("May the games begin. The following characters are present:\n")
    for c in chars:
        print(c)
        print('')

    game_over = False   
    turn = 0
    while not game_over:
        print("It's the turn of noble {0} {1}. Please select a player to attack:".format(chars[turn].c,chars[turn].name))
        possible = []
        for i in range(len(chars)):
            if not i==turn:
                possible.append(i)
                print(" - ({0}): {1} named {2}".format(i,chars[i].c,chars[i].name))
        sel = -1
        while not sel in possible:
            s = input('Selection: ')
            try:
                sel = int(s)
            except:
                print("That's not a valid choice")

        chars[turn].attack(chars[sel])
        if chars[sel].stats['HP']<=0:
            game_over=True
            print("That was it! {0} has died and the game is over.".format(chars[sel].name))
        turn +=1
        if turn==len(chars):turn=0        
