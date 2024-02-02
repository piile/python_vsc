#publiskie mainīgie
class Skolens:
    def __init__(self, vards):
        self.vards = vards #publisks mainīgais

skolens1 = Skolens("Anna")
print(skolens1.vards) #tieša piekļuve publiskajam mainīgajam

#ar privāto mainīgo
class Students:
    def __init__(self, vards):
        self.__vards = vards #privātais mainīgais

    def iegut_vardu(self):
        return self.__vards

students1 = Students("Alise")
# print(students1.__vards)
print(students1.iegut_vardu())
