import random
play_again="yes"
while play_again=="yes":

    user_attempt=0
    guess=range(0,101)
    target=random.randint(0,100)

    print(f"  number guessing game ")
    while True:
       try:
        user_choice=int(input(f" GUESS A NUMBER: "))
       except ValueError:
         print(f" INVALID CHOICE")
         continue
   
       if user_choice not in guess:
        print(f" INVALID CHOICE")
        continue
       else:
        user_attempt+=1
        if user_choice==target:
          print(f" CORRECT! You guessed it in {user_attempt} attempts.")
          play_again=input(f" PLAY AGAIN? (yes/no): ").lower() 
          break  
        elif user_choice>target:
         print(f" high ")
        else :
         print(f" low ") 