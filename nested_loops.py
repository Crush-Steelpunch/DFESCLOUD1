cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

for outerloopVar in cool_animals:
    for innerloopVar in outerloopVar:
        if innerloopVar == 'Milkshake':
            break 
        print(innerloopVar)
