import random
import time
from getpass import getuser


username = getuser()

currentBalance = 0

print(f"Welcome to Infissino Casino, {username}! Surely u are not gonna lose all yr money today!")

def playHeadsTails():
    global currentBalance
    HEADS = "heads"
    TAILS = "tails"
    COIN_VALUES = [HEADS, TAILS]

    print("Welcome to Heads&Tails!")
    side = input("Would you rather bet on Heads or Tails: ")
    if side.lower() in ["heads", "tails"]:
        sideBet = int(input("How much money would you like to bet? "))
        if sideBet > currentBalance:
            print(f"Your balance is {currentBalance} but you are trying to bet {sideBet}")
            time.sleep(1)
            startMenu()
        print(f"You bet {sideBet} $ on {side}")
        time.sleep(1)
        flipCoin = random.choice(COIN_VALUES)
        print("Flipping", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="")
        print()
        if side == flipCoin:
            print("Congrats! You win!")
            prizeMoney = sideBet * 2
            currentBalance += prizeMoney
            time.sleep(2)
            startMenu()
        else:
            print("Maybe next time...")
            currentBalance -= sideBet
            time.sleep(2)
            startMenu()
    else:
        print("Only Heads or Tails are allowed")
        playHeadsTails()

def playRoulette():
    global currentBalance
    print("Welcome to a roulette!")
    print("specific number or 0 is x36")
    print("Its time for making bets!")
    bet = int(input("What would u like to bet on: (write specific number or 0): "))
    if bet > 36:
        print("You can't bet more than 36")
        time.sleep(2)
        playRoulette()

    moneyBet = int(input(f"How much money would you like to bet on {bet}: "))


    if moneyBet < 0:
        print(f"Your bet must be grater than 0 $")
        time.sleep(2)
        playRoulette()
    elif moneyBet > currentBalance:
        print(f"You have {currentBalance} $ but your bet is {moneyBet} $")
        time.sleep(2)
        startMenu()
    else:
        print(f"You bet on {bet} - {moneyBet} $")
        print("Spinning", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="")
        print()
        time.sleep(3)
        spin = random.randint(0,36)
        print(f"We have got {spin} !")
        if bet == spin:
            print("Congrats!")
            winMoney = moneyBet * 36
            currentBalance += winMoney
            time.sleep(1)
            startMenu()
        else:
            print("Maybe next time (")
            currentBalance -= moneyBet
            time.sleep(1)
            startMenu()

def withdrawMoney():
    global currentBalance
    withdraw = int(input("How much money would you like to withdraw? "))
    withAuth = input(f"You have entered: {withdraw} is it correct? (y/n)")
    if withAuth == "y":
        if withdraw > currentBalance:
            print(f"You want to withdraw {withdraw} $ but your balance is only {currentBalance} $")
            time.sleep(1)
            startMenu()
        elif withdraw <= currentBalance:
            print("Authorizing", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="")
            print()
            currentBalance -= withdraw
            time.sleep(2)
            print("You have successfully withdrawn your money!")
            print(f"Your current balance is {currentBalance} $")
            time.sleep(2)
            startMenu()
    elif withAuth == "n":
        withdrawMoney()
    else:
        startMenu()


def depositMoney():
    global currentBalance
    deposit = int(input("Enter how much money you want to deposit: "))
    depAuth = input(f"You have entered: {deposit} is it correct? (y/n)")
    if depAuth == "y":
        print("Authorizing", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="")
        print()
        currentBalance += deposit
        print("You have succesfully deposited your money!")
        print(f"Your current balance is {currentBalance} $")
        time.sleep(2)
        startMenu()
    elif depAuth == "n":
        depositMoney()
    else:
        startMenu()


def startMenu():
    print("""Menu:
      1. Play a roulette
      2. Play Heads and Tails
      3. Show My Current Balance
      4. Deposit Money
      5. Withdraw Money
      6. Exit""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        playRoulette()

    elif choice == 2:
        playHeadsTails()

    elif choice == 3:
        print(f"Your current balance is {currentBalance} $")
        time.sleep(3)
        startMenu()

    elif choice == 4:
        depositMoney()

    elif choice == 5:
        withdrawMoney()

    elif choice == 6:
        print(f"Bye, {username}! I hope u lost all yr money today!")
        time.sleep(2)

startMenu()
