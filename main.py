wrong = 0
answer1 = str(input("The best teasm in the 22/23 season: "))
if answer1 == 'Manchester City':
    print("Correct answer")
elif answer1 == 'Man City':
    print("Correct answer")
else :
    wrong = wrong + 1
    Correct = 'Manchester City'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

answer2 = str(input("Who is the best football player in the world?: "))
if answer2 == 'Lionel Andres Messi':
    print("Correct Answer")
elif answer2 == 'Messi':
    print("Correct answer")

else:
    wrong = wrong + 1
    Correct = 'Lionel Andres Messi'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

answer3 = str(input("Who was the best player in the 2022 World Cup Final?: "))
if answer3 == 'Mbappe':
    print("Correct answer")
elif answer3 == 'mbappe':
    print("Correct answer")
else :
    wrong = wrong + 1
    Correct = 'Mbappe'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

answer3 = str(input("Who was the best player in the 2022 World Cup Final?: "))
if answer3 == 'Mbappe':
    print("Correct answer")
elif answer3 == 'mbappe':
    print("Correct answer")
else :
    wrong = wrong + 1
    Correct = 'Mbappe'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

answer4 = str(input("The team that Ronaldo plays in: "))
if answer4 == 'Al Nassr':
    print("Correct answer")
elif answer4 == 'al nassr':
    print("Correct answer")
else :
    wrong = wrong + 1
    Correct = 'Al Nassr'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

answer5 = str(input("The best football anime: "))
if answer5 == 'Blue Lock':
    print("Correct answer")
elif answer5 == 'blue lock':
    print("Correct answer")
elif answer5 == 'bluelock':
    print("Correct Answer")
else:
    wrong = wrong + 1
    Correct = 'Blue Lock'
    print("Wrong Answer " + "Correct Answer is " + str(Correct))

if wrong <= 0:
    print("Wow! You got nothing wrong")

else: wrong <= 0
print("You got " + str(wrong) + "Questions Wrong")