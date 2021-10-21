import random

class Dice():

    def __init__(self,dieSides):
        self.dieSides = dieSides


    def roll(self):
        return self._rollgen()

    def _rollgen(self):
        return random.randint(1,self.dieSides)

attack_roll = Dice(10)
#attack_roll.dieSides = 10
print(attack_roll.dieSides)
def_roll = Dice(4)
#def_roll.dieSides = 4

charisma = Dice(7)
print(charisma.dieSides)

print(attack_roll.roll())
print(getattr(charisma, "dieSides"))


#help(str)