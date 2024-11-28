import random 
print("hi  welcome to the GUESSING game.\n You got 5 chances to do it. \n Let's Go.")

num = random.randrange(10)
print(num)
chances = 5 
while (chances>0):
    guess=int(input("Hey Guess the correct number (1-10):")) 
    if guess> num :
        print("Try Again! You guessed too high")
        chances-=1 
    elif guess<num :
        print("Try Again! You guessed too low")
        chances-=1
    else:
        print("Congratulations")
        break 
if chances == 0 :
    print("Oops you lost the game.")


    
