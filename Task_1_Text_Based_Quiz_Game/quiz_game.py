print("================================")
print("       WELCOME TO QUIZ GAME")
print("================================")

score = 0

print("\nAnswer the following questions:\n")

# Question 1
print("1. Which language is used for web page structure?")
print("A. Python")
print("B. HTML")
print("C. Java")
print("D. C++")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B.")

# Question 2
print("\n2. Which keyword is used to define a function in Python?")
print("A. function")
print("B. define")
print("C. def")
print("D. fun")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is C.")

# Question 3
print("\n3. Which data type is used to store True or False?")
print("A. String")
print("B. Boolean")
print("C. Integer")
print("D. Float")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is B.")

# Question 4
print("\n4. Which symbol is used for comments in Python?")
print("A. //")
print("B. <!-- -->")
print("C. #")
print("D. **")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is C.")

# Question 5
print("\n5. Which company developed Python?")
print("A. Microsoft")
print("B. Google")
print("C. Apple")
print("D. Python Software Foundation")

answer = input("Enter your answer: ").upper()

if answer == "D":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is D.")

print("\n================================")
print("           QUIZ RESULT")
print("================================")

print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent! You got all answers correct.")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again.")

print("================================")
print("        THANK YOU FOR PLAYING")
print("================================")