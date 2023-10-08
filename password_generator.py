import random
from string import ascii_letters, digits, punctuation


class Password:
    """Password Generator

    strength=low, default length=8, input=letters
    strength=mid, default length=12, input=letters+digits
    strength=high, default length=16, input=letters+digits+punctuations
    default strength=mid, length=12, input=letters+digits
    """

    def __init__(self, strength="mid", length=None):
        self.strength = strength.lower()
        self.length = length
        self.generated = None

    def generate_password(self):
        if self.strength == "low":
            if self.length is not None:
                self.generated = Low(self.length)
                return self.generated.generate_password()

            self.generated = Low()
            return self.generated.generate_password()

        if self.strength == "mid":
            if self.length is not None:
                self.generated = Mid(self.length)
                return self.generated.generate_password()

            self.generated = Mid()
            return self.generated.generate_password()

        if self.strength == "high":
            if self.length is not None:
                self.generated = High(self.length)
                return self.generated.generate_password()

            self.generated = High()
            return self.generated.generate_password()


class BaseLevel:
    """Parent class for password generating class"""

    def __init__(self, length):
        self.length = length
        self.password = []
        self.choice_universe = None

    def generate_password(self):
        try:
            self.password = random.choices(population=self.choice_universe, k=self.length)
        except TypeError:
            print("Choice Universe not chosen")

        else:
            return "".join(self.password)


class Low(BaseLevel):
    def __init__(self, length=8):
        super().__init__(length)
        self.choice_universe = ascii_letters


class Mid(BaseLevel):
    def __init__(self, length=12):
        super().__init__(length)
        self.choice_universe = ascii_letters + digits


class High(BaseLevel):
    def __init__(self, length=16):
        super().__init__(length)
        self.choice_universe = ascii_letters + digits + punctuation


p1 = Password("low", 30)
print(p1.generate_password())
p2 = Password()
print(p2.generate_password())
p3 = Password("high",30)
print(p3.generate_password())
