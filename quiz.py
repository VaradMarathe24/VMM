# Basic Python Program

# Taking input from the user
name = input("Enter your name: ")
coo=input("Enter your nationality:-" )
age = int(input("Enter your age: "))

# Simple Cricket Quiz in Python

score = 0

print("Welcome to the Cricket Quiz!\n")

# Question 1
print("1. Who is known as the 'God of Cricket'?")
print("a) Virat Kohli\nb) Sachin Tendulkar\nc) MS Dhoni\nd) Rohit Sharma")
answer1 = input("Your answer: ").strip().lower()
if answer1 == 'b' or answer1 == 'sachin tendulkar':
    score += 1

# Question 2
print("\n2. How many players are there in a cricket team?")
print("a) 10\nb) 11\nc) 12\nd) 9")
answer2 = input("Your answer: ").strip().lower()
if answer2 == 'b' or answer2 == '11':
    score += 1

# Question 3
print("\n3. Which country won the ICC Cricket World Cup in 2011?")
print("a) India\nb) Australia\nc) England\nd) Sri Lanka")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'a' or answer3 == 'india':
    score += 1


# Question 3
print("\n4. Who won the orange cap of IPL 2008?")
print("a) Mitchell Marsh\nb) Shaun Marsh\nc) Yusuf Pathan\nd) MS Dhoni")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'b' or answer3 == 'Shaun Marsh':
    score += 1


# Question 5
print("\n5. Who was the Most Valuable Player of IPL 2017?")
print("a) Krunal Pandya\nb) Steve Smith\nc) Ben Stokes\nd) MS Dhoni")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'c' or answer3 == 'Ben Stokes':
    score += 1

# Final Score
print(f"\nYour final score is: {score}/5")
if score == 5:
    print("Excellent! You're a cricket champ!")
elif score == 4:
    print("Good job! You know your cricket.")
else:
    print("Keep learning. Cricket has a lot to offer!")
