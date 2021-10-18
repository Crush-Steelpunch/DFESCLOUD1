textVar1 = input('TYPE A TEXT: ')
#numVar1= int(input('TYPE A NUM: '))


if textVar1 == 'otto':
    print('hello otto')
elif textVar1 == 'alison':
    print('hello alison')
elif textVar1 == 'Andrew':
    print('Hello Andrew')
elif textVar1 == 'alison':
    print('alison has typed in today')
else:
    print('I do not know who you are but hello anyway')




#  AND       input0   |   input1   | result
#            ---------+------------+-------
#                false|     false  | false
#                false|     true   | false
#                true |     false  | false
#                true |     true   | true
              

#  OR        input0   |   input1   | result
#            ---------+------------+-------
#                false|     false  | false
#                false|     true   | true
#                true |     false  | true
#                true |     true   | true