import random

print(f"======================================")
print(f"=========\033[1mNUMBER GUESSING GAME\033[0m=========")
print(f"======================================")
user_attempt=0
target=random.randint(0,100)

while True:
    try:
        guess=int(input(f" GUESS A NUMBER: "))
    except ValueError:
        print(f" INVALID CHOICE")
        continue
    user_attempt+=1
    if guess==target:
       print(f" CORRECT! You get right in {user_attempt} attempts.")
       break    
    elif guess>target:
       print(f" high ")
    else :
       print(f" low ")

