#had a few errors here and there and had to change the flow between calculateWinner() and main() to debug easier
#full thursday was used for debugging and recording for README.etc

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
        
#I changed the program to return a value in the calcwinner, and calculate it in the main function itself
#found this easier to debug and manage if there were any problems
    

#game plays until the human player gets 5 points
#was going to make it until either party gets 5 points, ran out of time as we only had 2 classes to do this :)
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
 
