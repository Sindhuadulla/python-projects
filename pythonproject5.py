import time 

def count_down(user_input):
    while user_input:
        mins,secs=divmod(user_input,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end="\r")
        time.sleep(1)
        user_input-=1
    print("Fire in the hole")
user_input = int(input("length ofthe countdown:"))
count_down(user_input)
