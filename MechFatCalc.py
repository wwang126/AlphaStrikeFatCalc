import random

class Mech:
    def __init__(self, mech_armor, mech_structure, mech_case, mech_tmm, mech_weapon):
        self.armor = mech_armor
        self.structure = mech_structure
        self.case = mech_case
        self.tmm = mech_tmm
        self.engine = 1
        self.weapon = mech_weapon
    def alive(self):
        if self.structure > 0:
            return True
        else:
            return False
    def hit(self, roll, mod):
        if roll >= self.tmm + mod:
            self.damage()
            #print("Hit")
        if roll == 12:
            #print("Boxcars!")
            self.damage()
            self.crit()
    def damage(self):
        if self.armor > 0:
            self.armor -= 1
        else:
            self.crit()
            self.structure -= 1
    def crit(self):
        roll = random.randint(1,6)
        roll += random.randint(1,6)
        #print("Crit! " + str(roll))
        if roll == 2:
            #print("Ammo Crit")
            if self.case == 0:
                self.structure = 0
                self.armor = 0
                #print("Mech Dead")
            if self.case == 1:
                self.damage();
        if roll == 7:
            if self.tmm > 0:
                self.tmm -= 1
                #print("Motive Damage TMM now " + str(self.tmm))
        if roll == 12:
            #print("Mech had " + str(self.armor) + str(self.structure) + " left")
            self.structure = 0
            self.armor = 0
            #print("Mech Dead")
        if roll == 6 or roll == 8:
            if self.weapon < 1:
                self.damage()
                #print("No Weapons, taking extra damage")
            else:
                self.weapon -= 1
        if roll == 3 or roll == 11:
            if self.engine == 0:
                self.structure == 0
                self.armor == 0
                #print("Engine Crit 2, mech destroyed")
            else:
                self.engine -= 1


def kill_mech(mech_armor, mech_structure, mech_case, mech_tmm, mod, mech_weapon):
    m1 = Mech(mech_armor, mech_structure, mech_case, mech_tmm, mech_weapon)
    rolls = 0
    while m1.alive():
        rolls += 1
        roll = random.randint(1,6)
        roll += random.randint(1,6)
        #print("rolled: " + str(roll))
        m1.hit(roll,mod)
    #print("Mech took " + str(rolls) + " dice to kill")
    return rolls

mech_structure = int(input("Mech Structure: "))
mech_armor = int(input("Mech Armor: "))
mech_tmm = int(input("Mech TMM: "))
mech_case = int(input("Mech Case 0-None 1-CASE 2-CASEII: "))
mech_weapon = int(input("Mech Highest Weapon: "))
mod = int(input("Attacker modifier ex. 6 for medium, 4 for close: "))
count = 1000
dice_to_kill = 0
while count > 0:
    count -= 1
    dice_to_kill += kill_mech(mech_armor,mech_structure,mech_case,mech_tmm,mod,mech_weapon)
print("Average Dice to Kill: " + str(dice_to_kill/1000))