import random as rd
import time as tm

class RPS:
    def __init__(self):
        print("Rock, Paper, Scissors... Shoot!")

    def modes(self):
        return "1. Normal Mode, 2. Best Mode, 3. Blitz"

    username = input("Name -> ")

    random_choice = ['Rock', 'Paper', 'Scissors']
    valid_rock = ['R', 'r', 'Rock', 'ROCK', 'rock']
    valid_paper = ['P', 'p', 'Paper', 'PAPER', 'paper']
    valid_scissor = ['S', 's', 'Scissors', 'SCISSORS', 'scissors']
    winList, winId = [], []

    def rules(self, state1: str, state2: str):
        """
            State1 -> :return: User
            State2 -> :return: Computer
        """
        if (state1 in self.valid_rock and state2 in self.valid_rock) or (state1 in self.valid_paper and state2 in self.valid_paper) or (state1 in self.valid_scissor and state2 in self.valid_scissor):
            print("It's a Tie!")
        if state1 in self.valid_rock and state2 in self.valid_paper:
            self.winList.append(state2); self.winId.append('AI')
            print(f"Computer AI -> {state2} <- Wins!")
        if state1 in self.valid_rock and state2 in self.valid_scissor:
            self.winList.append(state1); self.winId.append(str(self.username))
            print(f"{self.username} -> {state1} <- Wins!")
        if state1 in self.valid_paper and state2 in self.valid_rock:
            self.winList.append(state1); self.winId.append(str(self.username))
            print(f"{self.username} -> {state1} <- Wins!")
        if state1 in self.valid_paper and state2 in self.valid_scissor:
            self.winList.append(state2); self.winId.append('AI')
            print(f"Computer AI -> {state2} <- Wins!")
        if state1 in self.valid_scissor and state2 in self.valid_rock:
            self.winList.append(state2); self.winId.append('AI')
            print(f"Computer AI -> {state2} <- Wins!")
        if state1 in self.valid_scissor and state2 in self.valid_paper:
            self.winList.append(state1); self.winId.append(str(self.username))
            print(f"{self.username} -> {state1} <- Wins!")

    def normalMode(self):
        user_choice = input('[R/P/S] -> ')
        computer_choice = self.random_choice[rd.randint(0, 2)]
        self.rules(user_choice, computer_choice)

    def bestMode(self):
        print("""
            Options: -> 1. Best2of3, 2. Best3of5, 3. Best6of10
        """)

        def best2of3():
            for i in range(3):
                self.normalMode()
            print()
            if len(self.winId) == 1:
                print(f"{self.winId[0]} Wins this Round!")
            if self.winId.count(self.username) == self.winId.count("AI"):
                print("'Twas a Tie!")
            if self.winId.count(self.username) >= 2:
                print(f"{self.username} Wins this Round!")
            if self.winId.count('AI') >= 2:
                print(f"Computer AI Wins")


        def best3of5():
            for i in range(5):
                self.normalMode()
            print()
            if len(self.winId) == 1:
                print(f"{self.winId[0]} Wins this Round!")
            if self.winId.count(self.username) == self.winId.count("AI"):
                print("'Twas a Tie!")
            if self.winId.count(self.username) >= 3:
                print(f"{self.username} Wins this Round!")
            if self.winId.count('AI') >= 3:
                print(f"Computer AI Wins")

        def best6of10():
            for i in range(10):
                self.normalMode()
            print()
            if len(self.winId) == 1:
                print(f"{self.winId[0]} Wins this Round!")
            if self.winId.count(self.username) == self.winId.count("AI"):
                print("'Twas a Tie!")
            if self.winId.count(self.username) >= 6:
                print(f"{self.username} Wins this Round!")
            if self.winId.count('AI') >= 6:
                print(f"Computer AI Wins")

        bestChoice = input("BestChoice -> ")
        if bestChoice == '1':
            best2of3()
        elif bestChoice == '2':
            best3of5()
        elif bestChoice == '3':
            best6of10()
        else:
            print()
            self.bestMode()

    def blitzMode(self):
        _ques = input('Are U Ready: ')
        trials = int(input('Trials -> ')
        valid = ["Yes", "YES", "yes", "y", "Y"]
        check = lambda valid, _ques: True if _ques in valid else False
        if (check(valid, _ques)):
            for i in range(trials):
                self.normalMode()
                tm.sleep(0.1)


    _q = input('[Y/N]: ')


valid = ["Yes", "YES", "yes", "y", "Y"]
myRPS = RPS()
while True:
    if myRPS._q not in valid:
        break
    else:
        print(myRPS)
        print(myRPS.modes())
        choice = input('Mode -> ')
        if choice == '1':
            print(myRPS.normalMode())
        elif choice == '2':
            print(myRPS.bestMode())
        else:
            print(myRPS.blitzMode())
        print()
