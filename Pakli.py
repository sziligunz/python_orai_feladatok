import random as r

class Kartya:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.color} {str(self.number)}"


class Pakli:
    colors = ["pikk", "kőr", "káró", "treff"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.generate_pakli()

    def __str__(self):
        return str(len(self.cards))

    def generate_pakli(self):
        for color in Pakli.colors:
            for number in Pakli.numbers:
                self.cards.append(Kartya(color, number))

    def kavar(self):
        if len(self.cards) != 52:
            raise ValueError("Megkezdett pakli nem keverhető")
        r.shuffle(self.cards)
        return self

    def huzas(self):
        if len(self.cards) <= 0:
            raise ValueError("Egy tetszőleges szöveg")
        return self.cards.pop(self.cards.index(r.choice(self.cards)))


if __name__ == '__main__':
    p = Pakli()
    # Size at generation
    print(p)
    # Shuffle
    p.kavar().kavar().kavar()
    # Pulling
    print(p.huzas())
    # Size after pulling
    print(p)

    # test for Pakli::kavar() if there has been already at least one card removed
    try:
        p.kavar()
    except ValueError as e:
        print(f"An error has been occured: {str(e)}")

    # test for Pakli::huzas() if there is no more cards to choose from
    try:
        for i in range(52):
            p.huzas()
    except ValueError as e:
        print(f"An error has been occured: {str(e)}")
