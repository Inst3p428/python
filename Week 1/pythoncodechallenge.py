#1. Personalized Greeting App 👋
#Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
name=str(input("Enter name: "))
color=str(input("Enter favorite color: "))
print(f"Hello,{name}! Your favorite color,{color},is aweseome")
#2. Simple Quiz Game 🎮
#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆


while True:
    print("Quiz on CARS")
    print("Type'quit'to end")
    points=[]
    loses=[]
    total=0
    d_points=0
    Answers=["Toyota","Mitsubishi","Nissan","Mazda"]
    print(f"Which Japan car manufacture participates in WRC \n {Answers}")
    your_choice=str(input("What is your answer?: "))
    if your_choice  == "quit":
        break
    if your_choice == "Toyota":
        points.append(1)
        print("One point earned")
    else:
        loses.append(1)
        print("Wrong answer!!")
    Answers2=["R32","R33","R34","R35"]
    print(f"Which Japan car features a 3.8l v6\n {Answers2}")
    your_choice=str(input("What is your answer?: "))
    if your_choice == "R35":
        points.append(1)
        print("One point earned")
    else:
        loses.append(1)
        print("Wrong answer!!")
    Answers3=["Audi","Porsche","Mercedes","Maserati"]
    print(f"Which car is not made in Germany \n {Answers3}")
    your_choice=str(input("What is your answer?: "))
    if your_choice == "Maserati":
        points.append(1)
        print("One point earned")
    else:
        loses.append(1)
        print("Wrong answer!!")
    print("You have reached end of quiz")
    for c_points in points:
        total += c_points
    for d_points in loses:
        d_total += d_points
    if total == 3:
        print(f"Congratultions you won with {total} points!!")
    elif d_total == 3 or d_total == 2 :
        print(f"You lost with {d_total} points")
    else:
        print("Try Again and aim higher")     
#3. Random Joke Generator
#Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡

import random
myjokes=["Why does Python live on land? Because it is above C level","Why did the loop go to therapy? It had too many while issues.","Whats a Python devs favorite movie? The Exception Handler","I wrote a song about a Python list… its pretty append-ing","My code does not have bugs; it just develops unexpected features","My coding skills are a lot like Python errors: constantly raising exceptions",
         "Why do Python programmers prefer dark mode? Because light attracts bugs!"]
print(random.choice(myjokes))      
