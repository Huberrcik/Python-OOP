import random


class Coin:

    def __init__(self):
        print("utworzono monete")
        self.side = "orzel"

    def throw(self):
        x = random.randint(1, 2)
        print(x)
        if x == 1:
            self.side = "orzel"
        else:
            self.side = "reszka"

    def show_side(self):
        print(self.side)


if __name__ == '__main__':

    coin1zl = Coin()
    coin2zl = Coin()
    coin5zl = Coin()
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
    wygrane = 0
    przegrane = 0
    for z in range(100):
        saldo = 0
        while (1 == 1):
            coin1zl.throw()
            coin2zl.throw()
            coin5zl.throw()
            if coin1zl.side == "orzel":
                saldo += 1
                print(f"Wypadl orzel 1zl, saldo = {saldo}")
                if saldo == 20:
                    print(f"saldo = {saldo}, wygrales!")
                    wygrane += 1
                    break
                elif saldo > 20:
                    print(f"saldo = {saldo}, przegrales :(")
                    przegrane += 1
                    break
            if coin2zl.side == "orzel":
                saldo += 2
                print(f"Wypadl orzel 2zl, saldo = {saldo}")
                if saldo == 20:
                    print(f"saldo = {saldo}, wygrales!")
                    wygrane += 1
                    break
                elif saldo > 20:
                    print(f"saldo = {saldo}, przegrales :(")
                    przegrane += 1
                    break
            if coin5zl.side == "orzel":
                saldo += 5
                print(f"Wypadl orzel 5zl, saldo = {saldo}")
                if saldo == 20:
                    print(f"saldo = {saldo}, wygrales!")
                    wygrane += 1
                    break
                elif saldo > 20:
                    print(f"saldo = {saldo}, przegrales :(")
                    przegrane += 1
                    break
    print(f"wygrane = {wygrane}")
    print(f"przegrane = {przegrane}")
