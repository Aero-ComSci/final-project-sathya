#Needs Debugging (Lots of errors)

import random
score = 0

def compChoice():
    choices = ["r", "p", "s"]
    x = random.choice(choices)
    return x

def userChoice(): 
    while True:
        x = input("Enter Rock, Paper, or Scissors (R, P, S):").strip().lower()
        if x in ["r", "p", "s"]:
            return x
        else:
            print("Invalid input! Please Try Again.")

def calculateWinner(compChoice, userChoice, score):
    
    if compChoice == userChoice:
        print("It's a draw!")
        
    elif compChoice == "r" and userChoice == "p":
        print("Computer Loses! You win!")
        score = score +1
    
    elif compChoice == "p" and userChoice == "s":
        print("Computer Loses! You win!")
        score = score +1
        
    elif compChoice == "s" and userChoice == "r":
        print("Computer Loses. You win!")
        score = score +1
        
    elif compChoice == "p" and userChoice == "r":
        print("Computer wins. You lose!")
        score = score -1
    
    elif compChoice == "s" and userChoice == "p":
        print("Computer wins. You lose!")
        score = score -1
        
    elif compChoice == "r" and userChoice == "s":
        print("Computer wins. You lose!") 
        score = score -1
        
    else:
        print("Something went wrong. Try again! ")

    

def main(score, compChoice, userChoice, calculateWinner): 
    result = calculateWinner(compChoice, userChoice, score)
    print("The winner was " + result + "." + " Good Job!")
    print("Your Score was : " + score)
        
 
main()

