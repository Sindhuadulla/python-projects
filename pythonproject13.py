import random 

def getdigits(num):
    return [int(i) for i in str(num)]


def no_duplicates(num):
     nums=getdigits(num)
     if len(nums)==len(set(nums)):
         return True
     else:
         return False 


def generateNum():
    while True:
       num= random.randint(1000,9999)
       if no_duplicates:
           return num 
def numOfBullsCows(num,guess): 
    bull_cow = [0,0] 
    nums= getdigits(num) 
    guess_li = getdigits(guess) 
      
    for i,j in zip(nums,guess_li): 
          
        # common digit present 
        if j in nums: 
          
            # common digit exact match 
            if j == i: 
                bull_cow[0] += 1
              
            # common digit match but in wrong position 
            else: 
                bull_cow[1] += 1
                  
    return bull_cow
num = generateNum() 
tries =int(input('Enter number of tries: ')) 

while tries > 0: 
    guess = int(input("Enter your guess: ")) 
      
    if not no_duplicates(guess): 
        print("Number should not have repeated digits. Try again.") 
        continue
    if guess < 1000 or guess > 9999: 
        print("Enter 4 digit number only. Try again.") 
        continue
      
    bull_cow = numOfBullsCows(num,guess) 
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows") 
    tries -=1
      
    if bull_cow[0] == 4: 
        print("You guessed right!") 
        break
else: 
    print(f"You ran out of tries. Number was {num}")
