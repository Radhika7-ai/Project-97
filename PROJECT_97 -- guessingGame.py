import random 
print('Number guessing game')

#randiant is function which help geterating random numbers
#here radiant is used to genrate random numbers between 1 to 9
number=random.randint(1 ,9) 
chances = 0 #here chances are initialy kept o and then it would go upto 5

print("guess a number between 1 and 9")

while chances < 5:
    guess = int(input('enter your guess:-  '))
    if(guess == number) :
        print('congratulation YOU WON !!')
        break #break is used to break from loop using loop

    elif(guess < number) :
        print("Your guess was too low: Guess a number higher than", guess)
    else :
        print("Your guess was too high: Guess a number lower than", guess)
    
    chances += 1
    if not chances < 5 :
        print("YOU LOSE!!! The number is", number)
