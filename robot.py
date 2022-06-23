from Weapons import Weapon 

class Robot(self, name, Weapon):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.Weapon = Weapon("Plasme Rifle", 50)
        
    

    def attack_dino(self, dinosaurs_to_attack):
        dinosaurs_to_attack.health -= self.Weapon.attack_power
        print(f"{dinosaurs_to_attack.name} is down to {dinosaurs_to_attack.health} \n")

    def __str__(self) -> str:
        return f"Robot:{self.name} with {self.health}"


robot = Robot("Jarvis")

print(robot)




# Robot_one = Robot(' I-Robot')
# Robot_two = Robot(' Biggie')
# Robot_three = Robot(' Smalls')

