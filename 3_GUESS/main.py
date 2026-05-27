import random as r

print("Welcome on board!")

range=int(input("Give a number: "))
number=r.randint(1,range)

No_of_Guesses=0

while True:
         No_of_Guesses += 1

         user_guess = input("Enter your Guess: ")

         if user_guess.isdigit():
                  user_guess= int(user_guess)

         else:
                  print("Enter a number next time")

         if user_guess==number:
                 print("You Guessed it right!")
                 break
         elif user_guess<number:
                 print("The number to guess is Greater")
                 continue
         elif user_guess>number:
                 print("The number to guess is Smaller")
                 continue

         
print(f"You took {No_of_Guesses} guesses")