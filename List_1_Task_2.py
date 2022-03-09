"""
1. Create Coin class
2. Non-parametrized constructor should create {side} of coin
3. Method throw() - randomly changes side of coin
4. Method show_side() returns side of Coin
5. Create several Coin objects and evoke their methods to simulate 15 coin flips
6. 100 simulations of hazard game
"""

import random


class Coin:
    # creating constructor
    def __init__(self):
        print("utworzono monete")
        self.side = "orzel"

    # function that change side of coin
    def throw(self):
        x = random.randint(1, 2)
        print(x)
        if x == 1:
            self.side = "orzel"
        else:
            self.side = "reszka"

    # function that shows current side of coin
    def show_side(self):
        print(self.side)


if __name__ == '__main__':
    # creating coins
    coin1zl = Coin()
    coin2zl = Coin()
    coin5zl = Coin()
    # throws every coin 5 times and shows its side
    """
    for y in range(5):
        coin1.throw()
        coin1.show_side()
    for y in range(5):
        coin2.throw()
        coin2.show_side()
    for y in range(5):
        coin3.throw()
        coin3.show_side()
"""
    # counters for wins and looses
    wygrane = 0
    przegrane = 0
    # simulating 100 games
    for z in range(100):
        saldo = 0
        # infinite loop that is broke by condition in IF block, when {saldo} equals or is greater than 20
        while (1 == 1):
            coin1zl.throw()
            coin2zl.throw()
            coin5zl.throw()
            # first condition sets if {side} is "orzel" or "reszka"
            # if "orzel", then it adds value of coin to {saldo} variable
            if coin1zl.side == "orzel":
                saldo += 1
                print(f"Wypadl orzel 1zl, saldo = {saldo}")
            if coin2zl.side == "orzel":
                saldo += 2
            if coin5zl.side == "orzel":
                saldo += 5

            # second condition breaks loop and shows winning message if {saldo} equals 20
            print(f"Wypadl orzel 2zl, saldo = {saldo}")
            if saldo == 20:
                print(f"saldo = {saldo}, wygrales!")
                wygrane += 1
                break
            # third condition breaks loop and shows loosing message if {saldo} is greater than 20
            elif saldo > 20:
                print(f"saldo = {saldo}, przegrales :(")
                przegrane += 1
                break
    # printing amount of wins and looses
    print(f"wygrane = {wygrane}")
    print(f"przegrane = {przegrane}")
