with open("story.txt","r") as f:
          story = f.read()

words= set()

target_at_start= "<"
start_of_word= -1

for i,ch in enumerate(story):
        if ch == target_at_start:
                start_idx= i
                start_of_word= "i"


        if ch == ">" and start_of_word == "i":
                word = story[start_idx+1 : i]
                words.add(word)




for info in words:
        
        story = story.replace(f"<{info}>", input(f"{info}: "))

print(story)
