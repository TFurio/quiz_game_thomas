print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play =D")
score = 0

answer = input("What state was Thomas born? ")
if answer.lower() == "illinois":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Thomas was born in Illinois.")

answer = input("What countries has Thomas taught in? ")
if answer.lower() == "usa, south korea, france, and italy":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Thomas has taught in the USA, South Korea, France, and Italy.")

answer = input("What WebDev bootcamp did Thomas attend? ")
if answer.lower() == "le wagon":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Thomas attended Le Wagon.")

answer = input("Where did Thomas earn his Master's degree? ")
if answer.lower() == "university of kent":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Thomas graduated from the University of Kent in Paris.")

answer = input("What are some of Thomas' passions? ")
if answer.lower() == "sports, travel, and writing":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Thomas enjoys sports, travel, and writing.")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/5 * 100) + "%")