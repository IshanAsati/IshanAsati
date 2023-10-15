wrong = 0 # defines the variable 'wrong' and gives ther value 0
answer1 = str(input("Your question here: ")) # answer 1 a variable is equal to the input provided when the question is asked and the input is a string
if answer1 == 'Your answer': # checking if answer1 is equal to the actual answer
    print("Correct answer") # prints "Correct Answer" if the answer is correct
elif answer1 == 'the other acceptable answer': # if the statement above is false then checking if answer is equal to the other acceptable answer
    print("Correct answer") # prints "Correct Answer" if the answer is correct
else : # if none of the other are true
    wrong = wrong + 1 # adds 1 to the wrong variable
    Correct = 'Your answer' # defines and gives the correct answer as the value
    print("Wrong Answer " + "Correct Answer is " + str(Correct)) # prints "wrong answer and the correct answer is" + variable correct
# you can duplicate this as many times as needed with chaning the questions and the answer
if wrong == 0: # checking if wrong equal to 0
    print("Wow! You got nothing wrong") # prints "Wow! You got nothing wrong" if the statement above is true

else: wrong > 0 # if the above is false then it checks if wrong is bigger than 0
print("You got " + str(wrong) + "Questions Wrong") # prints how many you got wrong
