import random
play_again="yes"
while play_again=="yes":
    print(f"==========================================")
    print(f"=========\033[1mSTONE PAPER SCISSOR GAME\033[0m=========")
    print(f"==========================================")
    user_score=0
    computer_score=0
    choices=["stone","paper","scissors"]
    for round_number in range(1,4):
        print(f" \033[1mROUND NUMBER: {round_number}\033[0m")
        while True:
            user_choice=input(f" ENTER YOUR CHOICE (stone/paper/scissors): ").lower()
            if user_choice not in choices:
              print(f" INVALID CHOICE! PLEASE TRY AGAIN.")
              continue
              
            break

 
        computer_choice=random.choice(choices)
        print(f" COMPUTER CHOSE: {computer_choice}")
        if computer_choice==user_choice:
             print(f"TIE! No points awarded.")
        elif (user_choice=="stone" and computer_choice=="paper")or\
            (user_choice=="paper" and computer_choice=="scissors")or\
            (user_choice=="scissors" and computer_choice=="stone"):
             print(f" COMPUTER WON THIS ROUND!")
             computer_score+=1
        else:
            print(f" YOU WON THIS ROUND!")
            user_score+=1

    print(f"==========================================")
    print(f" YOUR SCORE = {user_score} | COMPUTER_SCORE = {computer_score}")
    print(f"==========================================")
    if user_score==computer_score:
        print(f" ITS A TIE! ")
       
    elif user_score>computer_score:
        print(f" YOU WIN THE GAME! ")
       
    else:
        print(f" COMPUTER WINS THE GAME! ")
    play_again=input(f" PLAY AGAIN? (yes/no): ").lower()   
    if play_again=="no":
        print(f" THANK YOU FOR PLAYING! GOODBYE!")
      
