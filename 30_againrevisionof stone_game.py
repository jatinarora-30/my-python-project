import random
play_again="yes"
while play_again=="yes":
  print(f"========================================")
  print(f"=======\033[1mSTONE PAPER SCISSORS GAME\033[0m========")
  print(f"========================================")
  user_score=0
  computer_score=0
  choices=["rock","paper","scissors"]
  for round_number in range (1,4):
        print(f" \033[1mROUND NUMBER: {round_number}\033[0m")
        while True:
            user_choice=input(f" ENTER YOUR CHOICE (rock/paper/scissors): ").lower()
            if user_choice in choices:
                break
            else:
                print(f" INVALID CHOICE! PLEASE TRY AGAIN.")
        

        computer_choice=random.choice(choices)
        print(f" COMPUTER CHOSE: {computer_choice}")
        if user_choice==computer_choice:
            print(f" ITS A TIE! ")
        elif(user_choice== "paper" and computer_choice == "scissors")or\
            (user_choice== "rock" and computer_choice == "paper")or\
            (user_choice== "scissors" and computer_choice == "rock"):
            print(f" COMPUTER WINS THIS ROUND!")
            computer_score+=1
        else:
            print(f" YOU WIN THIS ROUND!")
            user_score+=1

  print(f"========================================")
  print(f"==============\033[1mFINAL SCORE\033[0m===============")
  print(f"========================================")
  print(f" YOUR SCORE: {user_score} | COMPUTER SCORE: {computer_score}")
  if user_score==computer_score:
    print(f" ITS A TIE!")
    play_again=input(f" PLAY AGAIN? (yes/no): ").lower()
  elif user_score>computer_score:
    print(f" YOU WIN THE GAME!")
    play_again=input(f" PLAY AGAIN? (yes/no): ").lower()
  else:
    print(f" COMPUTER WINS THE GAME!")
    play_again=input(f" PLAY AGAIN? (yes/no): ").lower()