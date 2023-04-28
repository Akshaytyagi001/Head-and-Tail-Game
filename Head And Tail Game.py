import random

head = '''    


                               
         |      |  
         |      | 
         |------|  
         |      |  
         |      |  


'''

tail = '''
       
       
        _________
            |
            |
            |
            |
            | 



'''

action = [head, tail]
n=int(input("Enter the No. of trials : "))
i=1
player_score=0
cp_score=0
while i<=n:
    player_choice = int(input("What do you choose? Type 0 for Head and 1 for Tail\n"))
    while player_choice > 1 or player_choice < 0:
        player_choice = int(input("Enter valid input: "))
    print(action[player_choice])

    computer_choice = random.randint(0,1)
    print("Coin Got: ")
    print(action[computer_choice])


    if player_choice == 0 and computer_choice == 0:
        player_score=player_score+1
        print("YOU WON!")
    elif player_choice == 1 and computer_choice == 1:
        player_score=player_score+1
        print("YOU WON!")
    elif computer_choice == 0 and player_choice == 1:
        cp_score=cp_score+1
        print("YOU LOSE!")
    elif computer_choice == 1 and player_choice == 0:
        cp_score=cp_score+1
        print("YOU LOSE!")
    i=i+1
if(player_score>cp_score):
    print(f"You won with score:{player_score-cp_score}")
elif(cp_score>player_score):
    print(f"You lost with score:{cp_score-player_score}")
else:
    print("Game Draw")
    
    
#Created by Akshay Tyagi