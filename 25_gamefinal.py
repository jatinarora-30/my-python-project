import random           
play_again="yes"
while play_again=="yes":
 print(f"=================================================================")
 print(f"=======================STONE PAPER SCISSOR=======================")
 print(f"=================================================================")
 user_score=0
 computer_score=0
 choices=["stone","paper","scissor"]

 for round_number in range (1,4):
     print(f" ROUND NUMBER : {round_number}")
     While TRUE:
          user_choice=input(f" user_choice = ").lower()
          if user_choice in choices
           break
          else:
             print(f" INVALID CHOICE! PLEASE TRY AGAIN.")
  
     computer_choice=random.choice(choices)
     print(f" COMPUTER CHOICE = {computer_choice} ")
     if user_choice==computer_choice:
       print(f"TIEE!")
     elif (user_choice=="stone" and computer_choice=="scissor")or\
    (user_choice=="paper" and computer_choice=="stone")or\
    (user_choice=="scissor" and computer_choice=="paper"):
      print(f" YOU GOT A POINT!")
      user_score+=1
     else:
       print(f" COMPUTER GOT A POINT!")
       computer_score+=1

 print(f" =============FINAL SCORE=============")
 print(f" user_score=  {user_score} | computer_score ={computer_score}")
 if user_score>computer_score:
    print(f" YOU WON !")
    play_again=input(f" PLAY AGAIN ? = ")
 elif computer_score>user_score:
    print(f" COMPUTER WON ! BETTER LUCK NEXT TIME")
    play_again=input(f" PLAY AGAIN ? = ")
 else:
    print(f" TIE!")
    play_again=input(f" PLAY AGAIN ? = ")

  
     
  


 
   

   



