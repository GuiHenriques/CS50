class Vault:
    def __init__(self, gals=0, sicks=0, knuts=0):
        self.gals = gals
        self.sicks = sicks
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.gals} Galleons, {self.sicks} Sicks, {self.knuts} Knuts"
    
    def __add__(self, other):
        gals = self.gals + other.gals
        sicks = self.sicks + other.sicks
        knuts = self.knuts + other.knuts
        return Vault(gals, sicks, knuts)

    def __sub__(self, other):
        gals = self.gals - other.gals
        sicks = self.sicks - other.sicks
        knuts = self.knuts - other.knuts
        return Vault(gals, sicks, knuts)

    def __mul__(self, other):
        gals = self.gals * other.gals
        sicks = self.sicks * other.sicks
        knuts = self.knuts * other.knuts
        return Vault(gals, sicks, knuts)

    def __truediv__(self, other):
        gals = self.gals / other.gals
        sicks = self.sicks / other.sicks
        knuts = self.knuts / other.knuts
        return Vault(gals, sicks, knuts)


potter = Vault(25, 50, 100)
print(potter)
wesley = Vault(100, 50, 25)
print(wesley)

add = potter + wesley
print(add)
sub = potter - wesley
print(sub)
mul = potter * wesley
print(mul)
div = potter / wesley
print(div)
