from options import option1, option2, option3, option4


def Menu():
  print("1. Start")
  print("2. Help")
  print("3. Credits")
  print("4. Exit")

  userSelect = int(input("Enter Option Number: "))
  if userSelect == 1:
    option1()

  if userSelect == 2:
    option2()

  if userSelect == 3:
    option3()

  if userSelect == 4:
    option4()


Menu()
