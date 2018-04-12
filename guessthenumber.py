import random as rm

num = rm.randint(1,20)

numberofguesses=0

while numberofguesses<6:
	print("Input the number to be guessed")
    guess = int(input())
    numberofguesses = numberofguesses+1
    if guess < num:
        print("Your guess is Low")
    if guess>num:
        print("Your guess is High")
    if guess == num :
        break
if guess==num:
    print("Good job you guessed my number"+str(num))
if guess!=num:
    print("Try Again")
    
