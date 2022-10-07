import random
import weapons


class Combatant:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.ac = 0
        self.temp_ac = 0
        self.run = False
        self.com = ''
        self.initiative = 0
        self.STRmod = 0
        self.DEXmod = 0
        self.temp_acmod = 3
        self.prof = 2
        self.weapon = 0
        self.atk_message = 'Roll a d20'

    def roll_initiative(self):
        self.initiative = random.randint(1, 20) + self.DEXmod

    def reference(self):
        print(f'''Player reference:
    Name: {self.name}   HP: {self.hp}   AC: {self.ac}   
    Modifiers:
        STR: {self.STRmod}  DEX: {self.DEXmod}
    Initiative: {self.initiative}''')

    def command(self):
        self.com = input(f"{self.name}, type a command > ").lower()

    def attack(self, target):
        print(f'{self.name} attacks {target.name}!')
        atk = 0
        print('Rolling dice ...')
        atk = random.randint(1, 20) + self.STRmod + self.prof
        if atk >= target.ac and atk >= target.temp_ac:
            dmg = self.damage() + self.STRmod
            print(f'{target.name} takes {dmg} damage')
            target.hp -= dmg
            print("Ouch!")
        else:
            print(f'{self.name} missed')

    def defend(self):
        print(f'{self.name} prepares for an incoming attack')
        if self.temp_ac == 0:
            self.temp_ac = self.ac + self.temp_acmod
        else:
            pass

    def damage(self):
        dmg = 0
        return dmg


class Player(Combatant):
    def set_stats(self, name, hp, ac):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.prof = 0
        self.atk_message = 'Make an attack roll'

    def damage(self):
        dmg = int(input('Roll your damage > '))
        return dmg


class Gnoll(Combatant):
    def set_stats(self, name):
        self.name = name
        num_of_hit_dice = 5
        hit_points = 0
        while num_of_hit_dice > 0:
            hit_points += random.randint(1, 8)
            num_of_hit_dice -= 1
        self.hp = hit_points
        self.ac = 15
        self.temp_acmod = 2
        self.STRmod = 2
        self.DEXmod = 1

    def damage(self):
        dmg = weapons.spear()
        return dmg


class Skeleton(Combatant):
    def set_stats(self, name):
        self.name = name
        num_of_hit_dice = 2
        hit_points = 0
        while num_of_hit_dice > 0:
            hit_points += random.randint(1, 8)
            num_of_hit_dice -= 1
        self.hp = hit_points + 4
        self.ac = 13
        self.temp_acmod = 1
        self.STRmod = 0
        self.DEXmod = 2

    def damage(self):
        dmg = weapons.shortsword()
        return dmg


class Zombie(Combatant):
    def set_stats(self, name):
        self.name = name
        num_of_hit_dice = 3
        hit_points = 0
        while num_of_hit_dice > 0:
            hit_points += random.randint(1, 8)
            num_of_hit_dice -= 1
        self.hp = hit_points + 9
        self.ac = 8
        self.temp_acmod = 2
        self.STRmod = 1
        self.DEXmod = -2

    def damage(self):
        dmg = random.randint(1, 6)
        return dmg
