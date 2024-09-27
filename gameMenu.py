# This was a rough attempt at making an unofficial text-rpg port of star citizen
# it does look half-arsed... that's because I gave up this part in order to work on the actual menu code

import time
import random

print("Star Civilian: A text-based RPG")
print("===============================")
print("This game contains characters, ships and locations that are wip,")
print("imported from my unfinished sci-fi series.")
time.sleep(1)


def runMenu():
  input("Press Enter to begin!")
  username = str(input("Enter a username: "))
  time.sleep(1)
  print("Welcome to the 'verse,", username, "!")
  f = open("username.txt", "w")
  f.write(username)
  f.close()
  password = str(input("Enter the demo version password:"))
  if password == "SC_Demo123":
		print("Password Accepted")
		time.sleep(1)
		print("--------------------------")
		time.sleep(1)
    print("Loading Game..")
    print("Pre-Loading Assets..")
    time.sleep(2)
    print("Loading complete!")
    print("Enjoy!")



print("Incorrect password, resetting..")
      time.sleep(1)
      exit()
