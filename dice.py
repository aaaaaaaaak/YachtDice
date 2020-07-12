import random


class Dice:
    def __init__(self):
        self.__saved = {}
        self.__dice = {"dice1" : 0, "dice2" : 0, "dice3" : 0, "dice4" : 0, "dice5" : 0}


    def rollDice(self): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for die in self.__dice:
            self.__dice[die] = random.randint(1, 6)
    

    def saveDice(self, saveList): # 선택한 주사위의 값을 리스트로 받아서 처리
        if saveList == []:
            return
        for i in saveList:
            for key, value in self.__dice.items():
                if value == i:
                    self.__saved[key] = value
        for key in self.__saved.keys():
            del(self.__dice[key])
    

    def unsaveDice(self, unsaveList): # saved -> dice
        if unsaveList == []:
            return
        for i in unsaveList:
            for key, value in self.__saved.items():
                if value == i:
                    self.__dice[key] = value
        for key in self.__dice.keys():
            del(self.__saved[key])
    

    def printSaved(self):
        print("Saved =", self.__saved)
    

    def printDice(self):
        print("Dice =", self.__dice)


class Turn: # 점수 판정 및 주사위 합쳐서 구성
    dc = Dice()


    def roll(self, onUp):
        # if onUp == TRUE:
        self.dc.rollDice()

class Score: # 점수 판정, 핸드 랭크
    pass


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