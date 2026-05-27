print("Welcome to the Adventure! Make out of it alive!")


weapon=input("You are stuck in a war-zone,gotta choose a weapon (hammer/sword): ")

if weapon.lower() == "hammer":
         choice1 = input("You have chosen the hammer, a giant is marching towards, " \
         "attack him or submit (attack/submit): ")
         if choice1.lower() == "attack":
                 choice2=input("Do you want to attck his leg or the abdomen (leg/abdomen): ")
                 if choice2.lower() == "leg":
                         print("Congarts! the giant trembled, you WON!")
                 elif choice2.lower() =="abdomen":
                         print("Faah! The giant caught you, You Died!")
                 else:
                         print("Invalid! You LOST!")
                         
         elif choice1.lower() == "submit":
                 print("The enemy caught you and traded your head for dimes! You Lost")                      

         else:
                 print("Invalid! You LOST!")

if weapon.lower() == "sword":

         choice1 = input("You have chosen the sword, you are now a warrior, you have to go left, right or forward: ")

         if choice1.lower() == "left":
                 
                 choice2=input("The most fearsome general is charging towards, you wanna move aside or fight (move/fight): ")
                 if choice2.lower() == "move":
                         print("You got away, saved your life! but sadly remembered for a coward ):")
                 elif choice2.lower() =="fight":
                         print("You Died after courageously fighting the general and became a war hero,you died but WON!")
                 else: 
                           print("Invalid! You LOST!")
                         
         elif choice1.lower() == "right":
                 
                 print("You fought NPCs and survived, You WON!")                      

         elif choice1.lower() == "forward":
                 
                 choice2= input("You are encountered by large elephants! gotta choose turn back or charge (revert/attack): ")  
                 if choice2.lower() == "revert":
                         print("you turned back and were killed for being a traitor! You LOST!") 
                 elif choice2.lower() == "attack":
                         print("You managed to survive somehow but had your back crushed! You WON!")

                 else:
                            print("Invalid! You LOST!")
                         
         else:
                 print("Invalid! You LOST!")
                 