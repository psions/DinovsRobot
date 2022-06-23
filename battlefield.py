import random
from typing_extensions import Self
import fleet
import herd
import Robots
import dinosaurs


class battlfield:
    def __init__(self):
        self.fleet = fleet
        self.fleet = herd


    def run_game(self):
        self.welcome_to_the_game()
        self.team = self.choose_team
        self.battle()



    def  display_welcome(self):
        print('You Have Now Entered The Arena')

    
    def choose_team(self):
        choose_team = int(input(' Which faction will you choose?: (1) Robots; or (2) Dinosaurs'))
        if choose_team == 1:
            print(' Welcome to the future with the Robots and the Fleet')
            return choose_team
        else choose_team == 2:
            print(' Welcome to the stone age of the Dinosaur Herd')
            return choose_team


    def battle(self):
        random_turn = random.randint(1, 2)
        if random_turn == 1:
            print( 'The Fleet shall prevail!')
            random_turn = 1
        if random_turn == 2:
            print(' The Herd pushes ahead!')
            random_turn = 2


     if first_turn == 1:
         while len(self.fleet.Robots) > 0 and len(self.herd.dinosaurs) >0:

            self.Robot_turn()

            if self.fleet.Robots[0].health < = 0:
                print (f'{self.herd.dinosaurs[0].type} is dead.')
                self.herd.dinosaur.remove(self.herd.dinosaurs[0])
            elif self.fleet.Robots[0].health <= 0:
                print(f'{self.fleet.robots[0].name} is out.')
                self.fleet.Robots.remove(self.fleet.Robots[0]

            if len(self.fleet.Robots) == 0:
                self.display_winners_dinosaurs()
                return
            elif len(self.herd.dinosaurs) == 0:
                self.display_winner_robots()
                return

            
            self.dinosaurs_turn()

            if self.herd.dinosaurs[0].health <= 0:
                print(f'{self.herd.dinosaurs[0].type} is dead.')
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            elif self.fleet.robots[0].health <= 0:
                print(f'{self.fleet.robots[0].name} is out.')
                self.fleet.robots.remove(self.fleet.robots[0])

            if len(self.fleet.robots) == 0:
                self.display_winners_dinosaurs()
                return
            elif len(self.herd.dinosaurs) == 0:
                self.display_winners_robots()
                return


            elif first_turn == 2:
                while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                    if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:
                        
                         self.dino_turn()  

                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dinosaurs[0].type} is out.')
                        self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f'{self.fleet.robots[0].name} is out.')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) == 0:
                        self.display_winners_robots()
                        return

                        self.robo_turn()  

                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dinosaurs[0].type} is out.')
                        self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f'{self.fleet.robots[0].name} is out.')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) == 0:
                        self.display_winners_robots()
                        return
    

    def dinosaurs_turn(self):
        self.dinosaurs_opponent_option()
        self.herd.dinosaurs[0].attack_Robots(self.fleet.robots[0])

    def Robots_turn(self):
        self.Robots_opponent_option()
        self.fleet.Robots[0].attack_dinosaurs(self.herd.dinosaurs[0])


    def dinosaurs_opponent_option(self):
        x = 1
        for self in self.fleet.Robots:
            print(f'{self.name} has {self.health} health')
            x += 1
    
    def Robots_opponent_option(self):

        x = 1

        for self in self.herd.dinosaurs:
            print(f'{self.name} has {self.health} health')
            x += 1

    def display_winners_robots(self):

        if self.team == 1:
            print(" The  fleet has defeated the herd  You win!")
        if self.team == 2:
            print(" You lose.")


    def display_winners_dinosaurs(self):

        if self.team == 2:
            print(" The herd has defeated the fleet You win!")
        if self.team == 1:
            print("Rawr! You loser .")
