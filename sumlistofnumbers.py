import pdb
pdb.set_trace()

#Write a Python function to sum all the numbers in a list

strinNums = input('Input a list of numbers seperated by a space')
numList = strinNums.split(' ')
resultVar = 0

for i in numList:
    resultVar += int(i)

print(resultVar)
