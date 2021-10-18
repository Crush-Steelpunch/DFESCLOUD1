# Continue example

shoppingList = ['Meat','Vegetables','Beer','Cake','Peas']

for produce in shoppingList:
    if produce == 'Beer':
        continue
    print('I need to buy: ' + produce)

print('end of loop')