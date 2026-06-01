import random

print(f"====================================")
print(f"========\033[1mNUMBER GUESSING GAME\033[0m========")
print(f"====================================")
user_attempt=0
target=random.randint(1,100)

while True:
    try:
      guess=int(input(f" YOUR GUESS : "))
      user_attempt+=1 
    except ValueError:
      print(f" INVALID INTEGER") 
      continue

    if guess==target:
       print(f"YOU GUESSED IT IN {user_attempt} attempts ")
       break
    elif guess>target:
       print(f" TOO HIGH ")
    else:
       print(f" TOO LOW ")
