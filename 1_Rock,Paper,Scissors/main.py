import random

print('Welcome to our game (:')

options= ["rock","paper","scissors"]

OPTIONS= {"rock" : "scissors",
          "paper" : "rock",
          "scissors" : "paper"}


score = 0

i=0
while i<10:
         i+=1
         user_input=input("Choose from rock,paper,scissors or q to quit the game: ").lower()

         if user_input== "q":
                  break

         else: 
                random_number= random.randint(0,2)
                computer= options[random_number]


                # if user_input in OPTIONS:
                if computer == OPTIONS[user_input]:
                                print(f"Computer chose {computer} and you chose {user_input}")
                                print("You Won!")
                                score +=1

                #   if user_input.lower()=="rock" and computer=="scissors":
                #            print("You Won!")
                #            score +=1

                #   elif user_input.lower()=="paper" and computer=="rock":
                #            print("You Won!")
                #            score +=1

                #   elif user_input.lower()=="scissors" and computer=="paper":
                #            print("You Won!")
                #            score +=1

                elif user_input.lower() == computer:
                          print("It's a Draw")

                else:
                           print('You Lost!')
                  
print(f"Your scored {score} out of {i} times:")

if score<5:
        print("Better Luck Next time!")

else :
        print("Great Win")
