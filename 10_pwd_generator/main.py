import random
import string

print("Type the specifications of the password you want!\n" \
"You get to choose from 3 generated Passwords.")

min_length = int(input("Type the length of password: "))
digit= input("Do you want to add digits (y/n): ")
char= input("Do you want to add special_characters (y/n): ") 


letters = string.ascii_letters
numbers = string.digits
special = string.punctuation


def generate(length, num,special_char):
         characters = letters

         if num == "y":
                                    
                  characters += numbers

         if special_char == "y":
                           
                  characters += special

         pwd=""
         for i in range(length):
                  pwd += random.choice(characters)
                  # i += 1
         return pwd

passwords= list()
for i in range(3):
         while True:
                  password= generate(min_length,digit,char)
                  print(f"Your password {i+1} is : {password}")
                  break
         passwords.append(password)

# print(passwords)

user_pwd= int(input("Which of these you prefer (1-3): "))
print(f"Your password is {passwords[user_pwd-1]}")
print("Thanks for using Our software!")
