import random
print(f"======================================================================")
print(f"==========================STONE PAPER SCISSOR=========================")
print(f"======================================================================")
user_score=0
computer_score=0
choices=[ "paper","scissor","stone"]

for round_number in  range(1,4):
    print(f"ROUND NUMBER: {round_number}")
    user_choice=input("CHOOSE:PAPER,SCISSOR OR STONE: ").lower()
    computer_choice=random.choice(choices)
    print(f"COMPUTER CHOSE: {computer_choice}")

    if computer_choice==user_choice:
      print(f" TIE!")
    elif (user_choice=="stone" and computer_choice=="scissor")or\
     (user_choice=="paper" and computer_choice=="stone")or\
     (user_choice=="scissor" and computer_choice=="paper"):
      print(f" YOU GOT A POINT!")
      user_score+= 1
    else:
       print(f" COMPUTER GOT A POINT!")
       computer_score+=1
    
print(f"=====================\033[1mFINAL SCORE\033[0m=====================")
print(f"\tuser_score : {user_score}  | computer_score: {computer_score}")

if user_score>computer_score:
   print(f" YOU WONN!")
elif computer_score>user_score:
   print(f" COMPUTER WON! BETTER LUCK NEXT TIME")
else:
   print(f" TIEE!")



