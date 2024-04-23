print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() !="yes":
    quit()
print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print('ПРАВДА!')
    score +=1
else: 
    print("НЕ ПРАВДА!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('ПРАВДА!')
    score=score + 1
else: 
    print("НЕ ПРАВДА!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('ПРАВДА!')
    score +=1
else: 
    print("НЕ ПРАВДА!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('ПРАВДА!')
    score +=1
else: 
    print("НЕ ПРАВДА!")   
answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print('ПРАВДА!')
    score=score +1
else: 
    print("НЕ ПРАВДА!")

print("You got "+str(score)+" questions correct!")
print("You got "+str((score/5) * 100)+ "%.")