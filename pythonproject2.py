import random 
name=input("What is your name:")
print(f'Good luck {name}')

languages = list(input().split())

tobeguessed= random.choice(languages)

print("Guess the characters")
guesses=""
chances=2 


while chances>0 :
    failed=0
    for char in tobeguessed.lower():
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            
            failed+=1 
    if failed==0 :
        print("\nYou win ")
        print(f"The correct word is {tobeguessed}")
        break
    print()
    guess=input("Guess the character:")
    guesses+=guess 

    if guess not in tobeguessed:
        chances-=1 
        if chances>0:
            print("wrong")
            print(f"you have more {chances} chances")
           
        if chances==0 :
            print("You lost")
