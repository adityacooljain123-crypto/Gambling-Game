import random
import sys
import turtle
import time

def Blacklistcheck(name):
    blacklist = open("blacklist.txt", "r")
    blacklisted = blacklist.readlines()
    blacklist.close()

    for line in blacklisted:
        if name + "\n" == line:
            print("")
            print("You are not welcome here due to past issues")
            print("Please get out of here. You do not deserve to be here")
            sys.exit()

    else:
        return True


def response(anger, name):
    response = ["That is not a valid input. Please try again.",
                   "Come on, you can do better than that. Enter a valid input.",
                   "Seriously? That's not a valid input. Try again.",
                   "Are you even trying? Enter a valid input this time."]
    
    if anger == 4:
        print("I do not think your taking this seriously")
        print("Or you think this is just a game")
        print("Well it's not")
        time.sleep(3)
        print("You are not welcome here and therefore please get out.")
        blacklist = open("blacklist.txt", "a")
        blacklist.write(name + "\n")
        blacklist.close()
        sys.exit()
    else:
        print(response[anger])


def generateFunds(money):
    chance = random.randint(1, 1000)

    if chance <= 650:
        money = random.uniform(0.01, 30)

    elif chance >= 650:
        money = random.uniform(30.01, 200)

    elif chance >= 800:
        money = random.uniform(200.01, 1000)

    elif chance >= 900:
        money = random.uniform(1000.01, 5000)

    elif chance > 999:
        money = random.uniform(5000.01, 1000000)
    
    return money


def setMoney(name):
    val = False
    anger = 0
    off = False
    print("")
    print("")
    print("Please enter your desired funds.")
    while not val:
        while not off:
            try:
                print("Type 'r' to receive a random amount:")
                money = (input(""))
                print("")
                print("")

                if money != "r":

                    money = float(money)
                    if money <= 0:
                        response(anger, name)
                        anger += 1

                    else:
                        val = True
                        print(f"Thank you {name}, your funds have been set to ${money:.2f}")
                        print("")
                        anger = 0

                        return money
                    
                else:
                    money = generateFunds(money)
                    val = True
                    print(f"Thank you {name}, your funds have been set to ${money:.2f}")
                    return money
                

            except ValueError:
                response(anger, name)
                anger += 1






#                          |
#                          |
#                          |
### The Race game is below |
#                          |
#                          |
#                          V






def TheRace(col):
    RacerNo = 6
    finish = 300
    speed = 10
    
    
    t =[]
    pos = []
    window = turtle.Screen()
    window.setup(900, 700)

    for turtleNo in range(RacerNo):
        new = turtle.Turtle()
        new.pensize(3)
        new.pencolor(col[turtleNo])
        t.append(new)
        pos.append(0)

    drawFinish(finish, RacerNo)
    startingOrder(RacerNo, t)
    finishPos = Race(RacerNo, pos, finish, speed, col, t)
    return finishPos


def drawFinish(finish, RacerNo):
    ref = turtle.Turtle()
    ref.hideturtle()
    ref.penup()
    ref.left(90)
    ref.forward(finish)
    ref.right(90)
    ref.pendown()
    ref.forward(RacerNo * 50)
    ref.back((RacerNo * 50) + 50)


def startingOrder(RacerNo, t):
    for turtleNo in range(RacerNo):
        t[turtleNo].penup()
        t[turtleNo].forward(turtleNo * 50)
        t[turtleNo].pendown()
        t[turtleNo].left(90)


def Race(RacerNo, pos, finish, speed, col, t):
    random.seed()
    finished = 0 
    finishPos = []
    print("Results: ")
    while finished < RacerNo:
        for turtleNo in range(RacerNo):
            if pos[turtleNo] < finish:
                move = random.randint(1, speed)
                t[turtleNo].forward(move)
                pos[turtleNo] = pos[turtleNo] + move
                if pos[turtleNo] >= finish:
                    finished = finished + 1
                    finishPos.append(col[turtleNo])
                    print(finished, ":", col[turtleNo])
                    
    return finishPos
    





#                           |
#                           |
#                           |
### The Dice game is below  |
#                           |
#                           |
#                           V






def Dice(bet):
    print("")
    print("")
    Win = False
    diceNo =  random.randint(0, 2)
    OddsOrEvens = random.randint(0, 10000)
    timer(3, False)
    print("\n")
    print("rolls...")
    time.sleep(1)

    if OddsOrEvens <= 8500:
        Win = 0
    
    else:
        Win = 1

    rolledNo = RolledNo(Win, bet, diceNo)

    WinRatio = [Win, rolledNo]

    return WinRatio


def timer(timE, ndtime):

    if not ndtime:
        while timE > 0:
            sys.stdout.write('\r' + str(timE))
            sys.stdout.flush()
            time.sleep(1)
            timE -= 1


def RolledNo(Win, bet, diceNo):

    if Win == 0:

        if bet == 1:
            dice = [1, 3, 5]
            rolledNo = dice[diceNo]

        else:
            dice = [2, 4, 6]
            rolledNo = dice[diceNo]

    else:

        if bet == 1:
            dice = [2, 4, 6]
            rolledNo = dice[diceNo]

        else:
            dice = [1, 3, 5]
            rolledNo = dice[diceNo]

    return rolledNo
            

def GenNumber():
    Gen = random.randint(1, 1000)
    return Gen
    

def checkNum(guess, numberChoosen):
    
    if numberChoosen == guess:
        Bool = True
        HorL = "OnIt"

    else:
        Bool = False
        HorL = checkPlace(guess, numberChoosen)


    return Bool, HorL


def checkPlace(guess, numberChoosen):

    if numberChoosen < guess:
        return "higher"
    
    elif numberChoosen > guess:
        return "lower"






#                                 |
#                                 |
#                                 |
## The Battleships game is below  |
#                                 |
#                                 |
#                                 V






def gridSetup():
    ships = False
    AiGrid = [["X","A","B","C","D","E","F","G","H"],
              ["1"," "," "," "," "," "," "," "," "],
              ["2"," "," "," "," "," "," "," "," "],
              ["3"," "," "," "," "," "," "," "," "],
              ["4"," "," "," "," "," "," "," "," "],
              ["5"," "," "," "," "," "," "," "," "],
              ["6"," "," "," "," "," "," "," "," "],
              ["7"," "," "," "," "," "," "," "," "],
              ["8"," "," "," "," "," "," "," "," "]]
    ShipCount = 0
    while not ships:
        ShipCol = random.randint(1, 8)
        ShipRow = random.randint(1, 8)

        if AiGrid[ShipRow][ShipCol] == "O":
            continue
            
        else:
            AiGrid[ShipRow][ShipCol] = "O"
            ShipCount += 1



        if ShipCount == 3:
            ships = True

        else:
            ships = False

        
    return AiGrid                



    


#                          |
#                          |
#                          |
#####  Main Program Below  |
#                          |
#                          |
#                          V






cont = True
anger = 0
print("Welcome!!")
print("")
print("")
print("Let us gamble!!")
print("")
print("")
name = input("Enter your name: ")
NameValid = Blacklistcheck(name)

money = setMoney(name)

print("")
print("")

while cont: 

    if money <= 0:
        print("Awww, sorry but you have $0 funds left")
        print("Come back with some more funds to continue gambling!!")
        print("Better luck next time")
        sys.exit
    else:
        print(f"Great! Now {name}, select a game to play!!")
        print("1. Race")
        print("2. Dice Roll")
        print("3. Battle Ships")
        print("4. Exit....")
        game = input("")






    if game == "1":
        cont1 = False
        while not cont1:
            cont1 = False
            Betinput = False
            anger = 0
            print("")
            print("")
            print("Now lets get ready for the turtle race!!")
            print("")
            print("Here are the rules...")
            print("You will choose one of the racers")
            print(f"Then 50% of your funds will be taken.")
            print("If your racer finishes 1st, then you get double your money.")
            print(f"If they finish 2nd, then you recieve 20% increase in your betting funds.")
            print(f"Else, you will lose all 50% of your betting funds.")
            print("")
            time.sleep(3)
            input("are you ready? ")
            betmoney = money - (money * 0.5)
            col = ["red", "blue", "green", "peru", "purple", "orange"]
            print(f"Now {name}, you have currently betted ${betmoney:.2f}")
            print("")
            print("")
            print("Your racers are: ")
            for x in range(len(col)):
                print(str((x + 1)) + ". " + (col[x]))
            while not Betinput:
                print("which one will you bet on (input via typing)?")
                Bet = input("")

                if Bet in col:
                    print("")
                    print("")
                    finishPos = TheRace(col)
                    Betinput = True
                    anger = 0
                    if Bet == finishPos[0]:
                        print(f"Congratulations {name}!!! {finishPos[0]} won the race!!")
                        print("for winning the bet, you recieve double your money")
                        betmoneynew = betmoney * 2
                        
                    elif Bet == finishPos[1]:
                        print(f"Congratulations {name}!!! {finishPos[1]}, got 2nd position!!")
                        print(f"for getting 2nd place, you recieve 20% of your bet")
                        betmoneynew = betmoney + (betmoney * 0.2)

                    else:
                        BetPosi = finishPos.index(Bet)
                        print("Awww...")
                        print(f"Sorry but {Bet}, finsihed in {BetPosi}th place")
                        print(f"You lose 50% of your funds")
                        betmoneynew = 0


                    print(f"{name}, your previous funds before the game was {money:.2f}")
                    print("Your funds have been updating...")
                    time.sleep(2)
                    print(f"Your funds are {(betmoney + betmoneynew):.2f}.")
                    print("")
                    print("")
                    print("do you want to continue (y/n)?")
                    ans = input("")

                    if ans == "y":
                        money = betmoney + betmoneynew
                        betinput = False
                        cont1 = False

                    else:
                        money = betmoney + betmoneynew
                        betinput = True
                        cont1 = True
                
                else:
                    response(anger, name)
                    anger += 1

    elif game == "2":
        cont1 = False
        inputcorr = False
        anger = 0
        firsttime = 0
        while not cont1:

            while not inputcorr:
                cont1 = False
                print("")
                print("")
                try:
                    if firsttime == 0:
                        print("Welcome to the Dice game!!")
                        print("")
                        print("Choose from two modes (type in number):")
                        print("1. Odds or Evens")
                        print("2. Guess the Number")
                        firsttime = 1
                        gameDice = int(input(""))

                    else:
                        print("Choose from two modes (type in number):")
                        print("1. Odds or Evens")
                        print("2. Guess the Number")

                except ValueError:
                    response(anger, name)
                    inputcorr = False
                    anger += 1

                else:
                    inputcorr = True


            if gameDice > 2:
                response(anger, name)
                anger += 1
                inputcorr = False

            if gameDice == 1:
                betinput = False
                anger = 0
                print("")
                print("You have selected the dice game")
                print("")
                print("Here are the rules...")
                print("There is a six-sided dice.")
                print("You will bet on odds or evens")
                print("If the dice hits an even, you get double your funds")
                print("else, you will lose those funds")
                print("")
                time.sleep(3)    
                input("are you ready? ")
                betmoney = money * 0.5
                print(f"You have betted ${betmoney:.2f}")
                
                
                while not betinput:


                    print("Odds or Evens (input 'odds' or 'evens')?")
                    bet = input("")
                    OorE = ["odds", "evens"]


                    if bet == "odds" or bet =="Odds":
                        betinput = True
                        bet = 0
                        anger  = 0
                    
                    elif bet == "evens" or bet == "Evens":
                        betinput = True
                        bet = 1
                        anger = 0

                    else:
                        response(anger, name)
                        anger += 1

                WinRatio = Dice(bet)
                Win = WinRatio[0]
                NoRolled = WinRatio[1]
                

                if Win == 0:
                    print(f"Aww... Sorry {name} but you betted on {OorE[bet]}. ")
                    print(f"The dice however rolled a {NoRolled}")
                    print(f"You lose all your betted funds")
                    betmoneynew = 0

                else:
                    print(f"Congratulations {name}!! you betted on {OorE[bet]}")
                    print(f"The dice rolled a {NoRolled}")
                    print(f"You get double of your betted funds!!")
                    betmoneynew = betmoney * 2


                print(f"{name}, your previous funds before playing the game were ${money:.2f}")
                print(f"Your funds are being updated...")
                time.sleep(2)
                print(f"Your funds are ${(betmoney + betmoneynew):.2f}.")
                print(" ")
                print(" ")
                print("Do you want to continue another round (y/n)?")
                ans = input("")

                if ans == "y":
                    money = betmoney + betmoneynew
                    betinput = True
                    cont1 = True

                else:
                    money = betmoney + betmoneynew
                    betinput = True
                    cont1 = True
            
            elif gameDice == 2:
                betinput = False
                anger = 0
                print(" ")
                print("You have selected the Guess the number game")
                print(" ")
                print("Here are the rules...")
                print("There is a 1000-sided dice")
                print("I will roll a random number and choose that")
                print("You need to guess that number in under 5 guesses")
                print(f"50% of your funds will be added to the prize pool")
                print("If you get it under 5 guesses, you get rewarded the prize pool multiplyed by the remaining attempts")
                print("Else, you lose all the money added to the prize pool")
                time.sleep(3)
                input("are you ready? ")
                print(" ")
                betmoney = money * 0.5
                print(f"You have betted ${betmoney:.2f}")
                time.sleep(1)
                numberChoosen = GenNumber()
                tooMuch = False
                inputCorr = False
                guesses = 1
                WinOpp = True


                while not betinput:

                    while not tooMuch :

                        while not inputCorr:

                            try:

                                if guesses == 1:
                                    print(" ")
                                    print(f"What is your {guesses}st guess (1, 1000)?")
                                    guess =  int(input(""))

                                elif guesses == 2:
                                    print(" ")
                                    print(f"What is your {guesses}nd guess (1, 1000)?")
                                    guess = int(input(""))

                                else:
                                    print(" ")
                                    print(f"What is your {guesses}th guess (1, 1000)?")
                                    guess = int(input(""))


                                if guess > 1000:
                                    guess = "w"
                                    guess = int(guess)

                                elif guess < 0:
                                    guess = "w"
                                    guess =int(guess)


                            except ValueError:
                                response(anger, name)
                                print(" ")
                                anger += 1
                                inputCorr = False
                            
                            else:
                                inputCorr = True

                        Bool = checkNum(numberChoosen, guess)[0]
                        HorL = checkNum(numberChoosen, guess)[1]

                        if guesses >= 5:
                                tooMuch = True
                                betinput = True
                                WinOpp = False

                        
                        if WinOpp:

                            if not Bool:
                                print("Incorrect")
                                print(" ")


                                if HorL == "higher":
                                    print(f"The number I am thinking of is {HorL}")

                                elif HorL == "lower":
                                    print(f"The number I am thinking of is {HorL}")

                                guesses += 1
                                tooMuch = False
                                betinput = False
                                inputCorr = False

                            else:
                                print("Correct!!")
                                print(f"My number was indeed {guess}")
                                betinput = True
                                betmoneynew = betmoney * (5 - guesses)
                                WinOpp = False

                if tooMuch:
                    print("You have used up all 5 guesses")
                    print("You Lose...")
                    time.sleep(1)
                    print(f"My number was {numberChoosen}")
                    betmoneynew = 0

                print(f"Ok {name}, your previous funds before playing the game were ${money:.2f}")
                anger = 0
                print(f"Your funds are being updated...")
                money = betmoney + betmoneynew
                time.sleep(2)
                print(f"Your funds are now ${money:.2f}")
                print("")
                print("")
                print("do you want to continue another round (y/n)?")
                ans = input()

                if ans == "y":
                    cont1 = False
                    betinput = False

                else:
                    cont1 = True
                    betinput = True

    elif game == "3":
        cont1 = False
        while not cont1:
            cont1 = False
            betinput = False
            anger = 0
            print(" ")
            print(" ")
            print("Welcome to battleships!!")
            print(" ")
            print("Here are the rules...")
            print("I will place down 3 ships onto an 8 x 8 grid")
            print("Each ship will have 1 hitpoint")
            print(f"You will bet 50% of your money")
            print("Then you will have 3 attempts to try to destroy my ships")
            print("For every ship you sink, you will gain 1 extra turn")
            print("If you destroy all the AI's ships within the attempts, you get 3 times your betted funds")
            print("Else, you will lose all betted funds")
            time.sleep(3)
            input("are you ready  ")
            betmoney = money * 0.5
            print(f"You have betted ${betmoney:.2f}")
            time.sleep(3)
            AiGrid = gridSetup()
            TooMuch = False
            ShipsSunk = 0
            Hit = 3
            Win = False
            ABCind = ["A", "B", "C", "D", "E", "F", "G", "H"]

            while not TooMuch:

                while not betinput:

                    try:
                        print(" ")
                        print(" ")
                        print("Input the coordinate you want to Hit (From A-H and 1-8, input like 'A6' or 'F8')")
                        Coor = input()
                        Coor = Coor.upper()
                        
                        CoorArr = list(Coor)
                        CoorArr[1] = int(CoorArr[1])

                        if len(CoorArr) != 2:
                            response(anger, name)
                            anger += 1
                            betinput = False

                        elif CoorArr[0] not in ABCind:
                            response(anger, name)
                            anger += 1
                            betinput = False

                        elif CoorArr[1] > 8 or CoorArr[1] < 0:
                            response(anger, name)
                            anger += 1
                            betinput = False

                        else:
                            betinput = True
                            anger = 0

                    except TypeError:
                        response(anger, name)
                        anger += 1
                        betinput = False

                
                CoorNumRow = CoorArr[1]
                CoorNumCol = ABCind.index(CoorArr[0]) + 1

                if AiGrid[CoorNumRow][CoorNumCol] == "X":
                    print("You have already sunken this ship")
                    Hit = Hit - 1

                elif AiGrid[CoorNumRow][CoorNumCol] == "O":
                    print("HIT!!")
                    print("You have hit one of my ships")
                    Hit = Hit
                    ShipsSunk += 1
                    AiGrid[CoorNumRow][CoorNumCol] = "X"

                else:
                    print("Miss...")
                    Hit = Hit - 1

                if ShipsSunk >= 3:
                    print("You have sunken all my ships!!!")
                    TooMuch = True
                    Win = True
                    betinput = True

                elif Hit <= 0:
                    print("You have ran out of attempts")
                    TooMuch = True
                    Win = False
                    betinput = True

                else:
                    print(f"I have {3 - ShipsSunk} ships remaining")
                    TooMuch = False
                    Win = False
                    betinput = False

            
            if TooMuch:

                if Win:
                    print("YOU WIN!!!")
                    print(" ")
                    betmoneynew = betmoney * 3

                else:
                    print("You Lose..")
                    print(" ")
                    betmoneynew = 0

            time.sleep(2)
            print(f"Ok {name}, your funds before playing the game was ${money:.2f}")
            anger = 0
            print("Your funds are being updated...")
            money = betmoney + betmoneynew
            time.sleep(2)
            print(f"Your current funds are now ${money:.2f}")
            print(" ")
            print(" ")
            print("Do you want to replay the game? (y/n)")
            cont2 = input("")
            if cont2 == "y":
                cont1 = False
            
            else:
                cont1 = True

    else:
        print("Exiting application.....")
        time.sleep(2)
        print("Thanks for playing!!!")
        sys.exit()
