import leons_functions

resultVar = leons_functions.test_z(z )
x = 1000
y = 2000
z = x * y
resultVar = test_z(z,x)
print(resultVar[0], 'The value of Z was: ', resultVar[1])
z = y - x
resultVar = test_z(z)
print(resultVar[0], 'The value of Z was: ', resultVar[1])
z = y * (x/2)
resultVar = test_z(z)
print(resultVar[0], 'The value of Z was: ', resultVar[1])
z = x * x
resultVar = test_z(z)
print(resultVar[0], 'The value of Z was: ', resultVar[1])
z = y * y
resultVar = test_z(z)
print(resultVar[0], 'The value of Z was: ', resultVar[1])

