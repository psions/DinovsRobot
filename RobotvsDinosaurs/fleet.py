from Weapons import Weapons
from Robots import Robot

class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()

    
    def create_fleet(self):
        weapon_one = Weapons('Plasma Rifle', 25)
        weapon_two = Weapons('Tractor Cannon', 30)
        weapong_three = Weapons('Bey Blade', 45)

        robot_one = Robot('I-Robot')
        robot_two = Robot('Biggie')
        robot_three = Robot('Smalls')







# 'Plasme Rifle', 'Tractor Cannon', 'Bey_Blade'

# Robot_one = Robot(' I-Robot')
# Robot_two = Robot(' Biggie')
# Robot_three = Robot(' Smalls')
