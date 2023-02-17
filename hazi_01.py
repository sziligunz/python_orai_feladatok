from abc import abstractmethod, abstractproperty, ABC


class Labbeli(ABC):
    @property
    @abstractmethod
    def viselheto(self):
        pass

    def menosegi_faktor(self):
        return 0


class Cipo(Labbeli):
    def __init__(self, marka, szin, **kwargs):
        super().__init__(**kwargs)
        self.marka = marka
        self.szin = szin
        self.kopottsag = 0

    @property
    def viselheto(self):
        return self.kopottsag < 10

    def menosegi_faktor(self):
        return (len(self.marka) + len(self.szin)) // 2

    def visel(self):
        self.kopottsag += 1


class Converse(Cipo):
    def __init__(self, szin):
        super().__init__("Converse", szin)

    def menosegi_faktor(self):
        return super(Converse, self).menosegi_faktor() + 5


class Csizma(Labbeli):
    def __init__(self, szar_magassag, **kwargs):
        super().__init__(**kwargs)
        self.szar_magassag = szar_magassag
        self.lyukas = 0

    def hasznal(self, num):
        self.lyukas += 1 if num > 100 else 0

    @property
    def viselheto(self):
        return self.lyukas == 0


class HelloKittyCsizma(Cipo, Csizma):
    def __init__(self, szin):
        super().__init__(marka="Hello Kitty csizma", szin=szin, szar_magassag=25)

    @property
    def viselheto(self):
        return Csizma.viselheto.fget(self) and Cipo.viselheto.fget(self)
