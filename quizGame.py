print("Welcome To My computer Game!")

playing = input("do you want to play the game? ")
score = 0

if playing.lower() != "yes":
    quit()

print("ok lets play the game :)")

answer = input("what does CPU stand for?  ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("wrong answer")

answer = input("what does RAM stand for?  ")
if answer.lower() == "rondom access memory":
    print("correct!")
    score += 1
else:
    print("wrong answer")

answer = input("what does GPU stand for?  ")
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("wrong answer")

answer = input("what does ROM stand for?  ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("wrong answer")

print("you got " + str(score) + " points")
print("you got " + str(score/4 *100) + " %.")