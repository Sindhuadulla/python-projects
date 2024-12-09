import random 
from collections import Counter

companyNames = '''Microsoft ibm paypal flipcart google amazon bhartpe ola netflix apple facebook JPMorgan''' 

companyNames=companyNames.split(" ")

selectedword=random.choice(companyNames)  

if __name__=="__main__":
    print("Guess the word. HINT: word is a name of a company.")
    for i in selectedword:
        print("_",end=" ")
    print()

    letterGuessed = ''
    chances = len(selectedword) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
            

            if guess in selectedword:
                k=selectedword.count(guess)

                for _ in range(k):
                    letterGuessed+=guess 

            for char in selectedword:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(selectedword)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(selectedword)):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(selectedword)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')
        if chances <= 0 and (Counter(letterGuessed) != Counter(selectedword)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(selectedword))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
