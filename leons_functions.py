import random

def test_z(inNum):
    if inNum < 5:
        return ['Z was less than 5', inNum]
    else:    
        return ['Z was greater than 5',inNum]
    

def alphabeta(tango,whisky,gin):
    if tango > whisky:
        if whisky > gin:
            return whisky
        else: 
            return gin
    else:
        if whisky > gin:
            return whisky
        else:
            return gin 

def printilikepies():
    print('I like pies')

def dice():
    return random.randint(0,6)

def randint():
    return 7


def len():
    print('Hi I am Len')