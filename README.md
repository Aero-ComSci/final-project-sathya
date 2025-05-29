*code is all given (day 1 progress, day 2 progress, final code) in python files in this repository*
#here are screenshots of the code, video became too big :( 

*I wanted to use this code to show how I can fix the combo menu grade i have currently. Right now i have a mid grade because of minor errors on my combo menu code and wanted to show how i utilized functions, lists, and loops in this project to see if i can get a better grade on that. 

*I also got a 2.4/3 on 3.1.1 and 3.1.2 and i feel like this program showcases the skills needed to show how I have grown with functions and printing and basic python. 

<img width="369" alt="Screenshot 2025-05-29 at 10 39 57 AM" src="https://github.com/user-attachments/assets/453efa52-0530-4ecf-b090-06fb0e7639e2" />

<img width="373" alt="Screenshot 2025-05-29 at 10 40 09 AM" src="https://github.com/user-attachments/assets/276a3605-0bee-4649-af01-b47e72ef0af7" />

https://github.com/user-attachments/assets/e75d813b-9f43-47ba-bd68-a76a89acab66

**Who is this program for:**
 This program is designed for anyone looking for a simple and quick way to play Rock, Paper, Scissors. It provides a straightforward interactive experience for a single player against a computer opponent.

**What does the program do and what does it automate:**
 The program automates the classic game of Rock, Paper, Scissors by handling the computer's random choices and determining the winner of each round. It also automatically tracks and updates the scores for both the player and the computer throughout the game.


***CodeSamples***
______________________


```
#The Loop
 while True:
        x = input("Enter Rock, Paper, or Scissors (R, P, S):  ").strip().lower()
        if x in ["r", 'p', 's']:
            return x
        else:
            print("Invalid input! Please Try Again!")
```



```
#The List & usage part

    compChoice = ["r", "p", "s"]
    x = random.choice(compChoice)
    
```

```
#Using a function (Showing main from the code)

def main(): 
    score = 0
    compScore = 0
    while score < 5:   
        gameResult = calculateWinner(compChoice(), userChoice())
        if gameResult == "W":
            score= score + 1
        if gameResult == "L":
            compScore = compScore +1
    
        print("Score = " + str(score))      
    print("Your score is : " + str(score) + "points" + " and the computer scored: " + str(compScore) + "points!")
    
main()
 
```


