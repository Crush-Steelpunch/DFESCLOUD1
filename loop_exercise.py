#Write a while loop which asks for the names of 5 people, 
# and for each person prints their name followed by the text
#  "is awesome!"
count = 0


while count < 5:
    name = str(input("What is your name?"))
    innercount = 0
    while innercount < 5:
        print(name, "is awesome!")
        innercount += 1
    count += 1