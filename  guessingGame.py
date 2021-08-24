import random
print("Number guesing Game")
number = random.randint(1,9)
chances = 0
#Name
print("Guess a number between 1-9")

while chances <5:
  guess=input("Enter you guess")
  if guess == number:
    print("Yor WON!")
    break  
  elif guess <number:
    print('Your guess was to loo')
  else:
    print('Your guess is too close')
  chances+=1    

if not chances < 5:
  print("You loose!")