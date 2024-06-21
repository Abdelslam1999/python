print ("Welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer = input("what does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does LAN stand for? ")
if answer.lower() == "local area network":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct!")   
print("you got " + str((score / 5) * 100) + "%.")