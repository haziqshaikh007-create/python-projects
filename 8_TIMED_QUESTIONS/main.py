import random
import time

MIN_VAL= 2
MAX_VAL= 10
OPEARTORS= ["+","-","*"]

print("Get 10 Questions right as soon as possible... Good Luck!")
input("To start press Enter key: ")
print("------------")

start= time.time()

def generate_problem():
    for i in range(10):
                  i+=1
                  while True:
                           operator= random.choice(OPEARTORS)
                           num= random.randint(MIN_VAL,MAX_VAL)
                           num2= random.randint(MIN_VAL,MAX_VAL)
                           question= f"{num} {operator} {num2}"
                           answer= input(f"Question no {i} is {question} :  ")

                           if answer == str(eval(question)):
                                    break
                           else:
                                   continue
                           
                  print(f"Your score is  {i}")
                  
generate_problem()

stop=time.time()
total_time= stop - start

print(f"You last {round(total_time,2)} seconds!")


