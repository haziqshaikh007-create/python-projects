print('Welcome to our Game!')

playing=input('Do you want to play quiz? ')

score = 0

if playing != "yes" :
         quit()

else: 
         answer=input("What is the capital of Pakistan? ")
         if answer.lower() == "islamabad" :
                  print("Correct answer!") 
                  score +=1
         else:
                 print("Incorrect):")

         answer=input("What is 2 times 2? ")
         if answer.lower() == "4" :
                  print("Correct answer!") 
                  score +=1
         else:
                 print("Incorrect):")

         answer=input("Who is the GOAT? ")
         if answer.lower() == "messi" :
                  print("Correct answer!") 
                  score +=1
         elif answer.lower() == "ronaldo":
                 print("You are Retarted(:\nIncorrecto(: ")

         else:
                 print("Incorrect):")

         answer=input("Which colour is the ball in Test cricket? ")
         if answer.lower() == "red" :
                  print("Correct answer!") 
                  score +=1
         else:
                 print("Incorrect):")
                 
         answer=input("Who is the founder of Tesla? ")
         if answer.lower() == "elon musk" :
                  print("Correct answer!") 
                  score +=1
         else:
                 print("Incorrect):")

if score>=3:
         print('You are a genius!')
         print(f'You got {score} right.')

else:
        print('Better Luck Next Time')
        print(f'You got {score} right.')

