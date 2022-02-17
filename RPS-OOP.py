import random as rd
import datetime as dt

class RPS:
    def init(self):
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
        trials = int(input('Trials -> '))
        valid = ["Yes", "YES", "yes", "y", "Y"]
        check = lambda valid, _ques: True if _ques in valid else False
        if (check(valid, _ques)):
            for i in range(trials):
                now = dt.datetime.now()
                user_choice = input('[R/P/S] -> ')
                _now = dt.datetime.now()
                # Time Entry Speed to just a second in this blitzMode
                if ((u_choice for u_choice in user_choice) == '' or (len(u_choice) for u_choice in user_choice) == 0) and ((_now - now).seconds > 5):
                    user_choice = ''
                    self.winId.append("AI")
                else:
                    computer_choice = self.random_choice[rd.randint(0, 2)]
                    self.rules(user_choice, computer_choice)
        if len(self.winId) == 1:
            print(f"{self.winId[0]} Wins this Round!")
        if self.winId.count(self.username) == self.winId.count("AI"):
            print("'Twas a Tie!")
        if trials % 2 == 0:
            if self.winId.count(self.username) > ((trials/2)+1):
                print(f"{self.username} Wins this Round!")
            elif self.winId.count('AI') >= ((trials/2)+1):
                print(f"Computer AI Wins")
            else:
                pass
        else:
            if self.winId.count(self.username) > ((trials/2)+0.5):
                print(f"{self.username} Wins this Round!")
            elif self.winId.count('AI') >= ((trials/2)+0.5):
                print(f"Computer AI Wins")
            else:
                pass
        print()

    def runner(self, class_object: str):
        class_object = RPS()
        print(class_object.init())
        print(class_object.modes())
        choice = input('Mode -> ')
        if choice == '1':
            print(class_object.normalMode())
        elif choice == '2':
            print(class_object.bestMode())
        elif choice == '3':
            print(class_object.blitzMode())
        else:
            self.runner()

    _q = input('[Y/N]: ')

    @property
    def q(self):
        return self._q


valid = ["Yes", "YES", "yes", "y", "Y"]
RPS_Instance = RPS()
while True:
    if RPS_Instance.q not in valid:
        break
    else:
        RPS_Instance.runner('myRPS')
        print()

