import random
print("")
print("")


print("\033[0;96m"+"| | | | ___| | | ___ | | |")
print("\033[0;96m"+"| |_| |/ _ \ | |/ _ \| | |")
print("\033[0;96m"+"|  _  |  __/ | | (_) |_|_|")
print("\033[0;96m"+"|_| |_|\___|_|_|\___/(_|_)")

print("")

Hellos = ['Hello. Would you like to try my quiz about dinosaurs?','Hey there.Would you like to try my quiz about dinosaurs?','Hii.Would you like to try my quiz about dinosaurs?']

SCORE = 0

loop = True

while loop:
  print("\033[0;34m" + "\033[1m" + random.choice(Hellos))

  break
print("")

print("\033[0;93m"+"\033[1m"+"Question One!!!!!!!!!!")

print("")

QuestionAnswer1 = input("Was the Brachiosaurus a herbivore or a carnivore??   "+"\033[0;37m")

QuestionAnswer1 = QuestionAnswer1.lower()

if QuestionAnswer1 == 'herbivore':
  print("\033[0;92m"+"Correct Answer! The Brachiosaurus Was a herbivore.")
  SCORE = SCORE+1
  print("Your score is", SCORE)

else:
  print("\033[0;31m"+"Wrong, The brachiosaurus was a herbivore.")
  SCORE = SCORE-1
  print("your score",SCORE)

print("\033[0;93m"+"\033[1m"+"Time for Question 2!!!")
print("What is the name of the famous velociraptor in Jurrasic world Dominion?")
print("")

QuestionAnswer2 = input("\033[0;33m"+"\033[2m"+"\033[1m"+"A-Herculey,   B- Blue    C- Beta"+'\033[0;37m'   )

QuestionAnswer2 = QuestionAnswer2.upper()

if QuestionAnswer2 == 'B' or QuestionAnswer2 == 'b':
  print("\033[0;92m"+"Correct Answer!!!!!")
  SCORE = SCORE+1
  print("Your score is", SCORE)
else:
  print("\033[0;31m"+"Wrong Answer. The velociraptors name was Blue")
  SCORE = SCORE-1
  print("Your score is", SCORE)
print("")

print("\033[0;93m"+"\033[1m"+"Question 3!!!")
print("")
print("")
QuestionAnswer3 = input("What group were dinosaurs with long horns and neck frills in???"+"\033[0;37m") # Tbh i dont know the answer to this question  ;)
QuestionAnswer3 = QuestionAnswer3.lower()
if QuestionAnswer3 == "ceratopsians":
  print("\033[0;92m"+"Correct Answer!")
  SCORE = SCORE+1
  print("your score is", SCORE)
else:
  print("\033[0;31m"+"Wrong the group was called ceratopsians")
  SCORE = SCORE-1
  print("your score is", SCORE)
print("")

print("\033[0;93m"+"Get ready for a Bonus Question!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("This Question is worth 2 points!")
print("")

Bonus = input("What was the largest dinosaur to live?"+"\033[0;37m")

Bonus = Bonus.lower()
if Bonus == "argentinosaurus":
  print("\033[0;92m"+"Correct.")
  SCORE = SCORE +1
  print("your score is",SCORE)
else:
  print("\033[0;31m"+"Wrong. The largest Dinosaur was the Argentinosaurus")
  
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;93m"+"\033[1m"+"Les go for question 5!!!!!")
QuestionAnswer5 = input("\033[0;93m"+"\033[1m"+"True or False. Did the Tyranosaurus rex have short arms?"+"\033[0;37m")

QuestionAnswer5 = QuestionAnswer5.upper()

if QuestionAnswer5 == ("TRUE"):
  print("\033[0;92m"+"Correct")
  SCORE = SCORE+1
else:
  print("\033[0;31m"+"Wrong. Trex had short arms")
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;93m"+"Question Six!!!!!!!")
print("\033[0;93m"+"Which one of these dinosaurs is a herbivore?")
QuestionAnswer6 = input("\033[0;33m"+"\033[2m"+"\033[1m"+"A-Tyrannosaurus, B- Velociraptor, C-Triceratops"+"\033[0;37m")
QuestionAnswer6 = QuestionAnswer6.upper()
if QuestionAnswer6 == "C":
  print("\033[0;92m"+"Correct Answer!")
  SCORE = SCORE+1
  print("your score is",SCORE)

else:
  print("\033[0;31m"+"Wrong answer,The Triceratops was a herbivore.")
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;93m"+"Question 7!!!!!!!")
QuestionAnswer7 = input("\033[0;93m"+"Dinosaurs died dueto a disease called dinostrus... TRUE OR FALSE"+"\033[0;37m")

QuestionAnswer7 = QuestionAnswer7.upper()

if QuestionAnswer7 == "FALSE":
  print("\033[0;92m"+"Correct")
  SCORE = SCORE+1
  print("your score is",SCORE)
else:
  print("\033[0;31m"+"Wrong.The dinosaurs died due to a large asteroid.")
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;93m"+"Time for another bonus question ")
BonusTwo = input("What group did the allosaurus belong to?"+"\033[0;37m")
BonusTwo = BonusTwo.lower()
if BonusTwo == "theropods":
  print("\033[0;92m"+"Correct Answer!!!")
  SCORE = SCORE+2
  print("your score is",SCORE)

else:
  print("\033[0;31m"+"Wrong Answer. The Allosaurus belonged to a group called theropods....")
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;93m"+"Question numero 9!!!!!!!!!!!!!!!!!!!")
QuestionAnswer9 = input("What does Tyrannosaurus mean?"+"\033[0;37m")
QuestionAnswer9 = QuestionAnswer9.lower()
if QuestionAnswer9 == "tyrant lizard":
  print("\033[0;92m"+"Correct Answer")
  SCORE = SCORE+1
  print("your score is",SCORE)

else:
  print("\033[0;31m"+"Wrong Answer. It means Tyrant Lizard...")
  SCORE = SCORE-1
  print("your score is",SCORE)
print("\033[0;93m"+"Time for the last question....")
print("When did dinosaurs go extinct")
QuestionLast = input("\033[0;33m"+"\033[2m"+"\033[1m"+"A-400years ago... B-65million years ago... C-700billion years ago..."+"\033[0;37m")
QuestionLast = QuestionLast.upper()
if QuestionLast == "B":
  print("\033[0;92m"+"Correct")
  SCORE = SCORE+1
  print("your score is",SCORE)

else:
  print("\033[0;31m"+"Wrong answer.The dinosaurs died 65 million years ago...")
  SCORE = SCORE-1
  print("your score is",SCORE)

print("\033[0;34m" + "\033[1m" + "You Have Completed the quiz!")
print("\033[0;34m" + "\033[1m" + "Congrats!!! :D")
print("\033[0;34m" + "\033[1m" + "you got ",SCORE," questions correct")