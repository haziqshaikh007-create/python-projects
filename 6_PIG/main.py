import random as r

def roll():
           
           return r.randint(1,6)

players= input("Type the number of players (2-4): ")

if players.isdigit():
         players = int(players)
       
else:
        print("Invalid input. Please enter a number between 2 and 4.")
        quit()

player_scores= [0 for _ in range(players)]

while max(player_scores) <= 50:
        
    for player_idx in range(players):
         
         print(f"The current player is Player {player_idx+1}")
         current_score = 0
         

         while True:    

                  should_roll= input("Do you wanna roll (y): ")
                  if should_roll.lower() != "y":
                           break
                  
                  else: 
                        value = roll()   

                        if value == 1:
                                print("You rolled a 1! Your turn is over.")
                                current_score = 0        
                                break 
                        else:
                                print(f"You rolled a {value}")
                                current_score += value 
                                print(f"Your Current score is {current_score}")

         player_scores[player_idx] += current_score
         

print(f"Player {player_idx+1} won!")