class Dinosaurs:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 110
        self.attack_power = attack_power
        self.energy = 50
        self.attack_move = ('Stomp', 'Breath of Fire', 'Sacrifice')


    def Attack_robot(self, Robots_to_attack,):
        if self.energy > 5:
            while True:
                try:
                    attack_move = int(input(f'Move Type: (1) {self.attack_move[0]}, (2) {self.attack_move[1]} or (3) {self.attack_move[2]}.'))
                except ValueError:
                    continue
                if attack_move == 1:
                    print(f'{self.name} attacked {Robots_to_attack.name} with {self.attack_move[0]} ')
                    break
                elif attack_move == 2:
                    print(f'{self.name} attacked {Robots_to_attack.name} with {self.attack_move[1]}')
                    break
                elif attack_move == 3:
                    print(f'{self.name} attacked {Robots_to_attack.name} with {self.attack_move[2]}')
                    break

        
            self.energy -=10
            Robots_to_attack.health -= self.attack_power
            print(f'{self.name} energy equals {self.energy}')
            print(f'{Robots_to_attack.name} health equals {Robots_to_attack.health')





# Dino_one = Dinosaurs(' Little Foot')
# Dino_two = Dinosaurs(' Big Foot')
# Dino_three = Dinosaurs(' Shorty')