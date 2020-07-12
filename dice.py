import random

class Dice:
    saved = {}
    dice = {"dice1" : 0, "dice2" : 0, "dice3" : 0, "dice4" : 0, "dice5" : 0}

    def rollDice(self): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for die in self.dice:
            self.dice[die] = random.randint(1, 6)
    
    def saveDice(self, saveList): # 선택한 주사위의 값을 리스트로 받아서 처리
        if saveList == []:
            return
        for i in saveList:
            for key, value in self.dice.items():
                if value == i:
                    self.saved[key] = value
        for key in self.saved.keys():
            del(self.dice[key])
    
    def unsaveDice(self, unsaveList): # saved -> dice
        if unsaveList == []:
            return
        for i in unsaveList:
            for key, value in self.saved.items():
                if value == i:
                    self.dice[key] = value
        for key in self.dice.keys():
            del(self.saved[key])
    
    def printSaved(self):
        print("Saved = ", self.saved)
    
    def printDice(self):
        print("Dice = ", self.dice)


d = Dice()

d.printSaved()
d.printDice()
d.rollDice()

d.printSaved()
d.printDice()

saveList = list(map(int, input("Save Dice Input (int int int ...) : ").split()))
d.saveDice(saveList)

d.printSaved()
d.printDice()

unsaveList = list(map(int, input("Unsave Dice Input (int int int ...) : ").split()))
d.unsaveDice(unsaveList)

d.printSaved()
d.printDice()

d.saveDice(saveList)
d.unsaveDice(unsaveList)

d.printSaved()
d.printDice()