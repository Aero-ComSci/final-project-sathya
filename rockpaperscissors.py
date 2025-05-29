# This is the final code for the project. Day 2 is basically the same as this, but kept this as well :)

import random

def compChoice():
    compChoice = ["r", "p", "s"]
    x = random.choice(compChoice)
    return x

def userChoice(): 
    while True:
        x = input("Enter Rock, Paper, or Scissors (R, P, S):  ").strip().lower()
        if x in ["r", 'p', 's']:
            return x
        else:
            print("Invalid input! Please Try Again!")


def calculateWinner(compChoice, userChoice):
    if compChoice == userChoice:
        print("It's a draw!")
        
    elif compChoice == "r" and userChoice == "p":
        print("Computer Loses! You win!")
        return "W"
    elif compChoice == "p" and userChoice == "s":
        print("Computer Loses! You win!")
        return "W"
    elif compChoice == "s" and userChoice == "r":
        print("Computer Loses. You win!")
        return "W"
    elif compChoice == "p" and userChoice == "r":
        print("Computer wins. You lose!")
        return "L"
    elif compChoice == "s" and userChoice == "p":
        print("Computer wins. You lose!")
        return "L"
    elif compChoice == "r" and userChoice == "s":
        print("Computer wins. You lose!") 
        return "L"
    else:
        print("Something went wrong. Try again! ")
      
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
 
