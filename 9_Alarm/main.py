import time
import winsound

# Get alarm time from user
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

CLEAR = "\033[2J"
CLEAR_RETURN ="\033[H"

timer = (minutes * 60) + seconds

print(CLEAR)

while timer != 0:
         for i in range(timer):
                  while True :
                           timer -= 1
                           # print(timer)
                           seconds -= 1
                           if seconds >= 60:
                                   minutes += 1
                                   seconds= seconds % 60
                           if seconds == 0 and minutes >= 1:
                                   minutes= minutes - 1
                                   seconds = 59
                           print(f"{CLEAR_RETURN}")
                           print(f"Alarm will ring in: {minutes:02d}:{seconds:02d}")
                           break
                  time.sleep(1)

winsound.Beep(1000, 1000) 
