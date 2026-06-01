import random
play_again="yes"
while play_again=="yes":

  print(f"---------------------------------------")
  print(F"------ROCK,PAPER AND SCISSOR GAME------")
  print(f"---------------------------------------")
  choices=["rock","paper","scissor"]
  user_score=0
  computer_score=0

  for round_number in range (1,4):
    print(f" \033[1mROUND NUMBER : {round_number}\033[0m")
    user_choice=input(f" CHOOSE ROCK/PAPER/SCISSOR: ")
    computer_choice=random.choice(choices)
    print(f" COMPUTER CHOSE: {computer_choice}")
    if user_choice==computer_choice:
     print(f" ROUND: TIE")
    elif ( user_choice== "paper" and computer_choice=="scissor")or\
       ( user_choice== "rock" and computer_choice=="paper")or\
       ( user_choice== "scissor" and computer_choice=="rock"):
     print(f" COMPUTER GOT A POINT")
     computer_score+=1
    else:
      print(f" YOU GOT A POINT")
      user_score+=1
  print(f"======================================")
  print(f"=============FINAL SCORE==============")
  print(f"======================================")
  print(f"\033[1mUSER SCORE = {user_score} | COMPUTER SCORE = {computer_score}\033[0m")
  if user_score>computer_score:
     input(f" YOU WON! PLAY AGAIN ? = ").lower()
  elif computer_score>user_score:
     input(f" COMPUTER WON ! PLAY AGAIN ? = ").lower()
  else:
     input(f" TIE! PLAY AGAIN ? = ").lower()
