import random

class Dice:
    TRY = 3
    fieldFlag = False
    save = {}
    dice = {"dice1" : 0, "dice2" : 0, "dice3" : 0, "dice4" : 0, "dice5" : 0}

    def rollDices(self): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for i in range(self.TRY):
            for die in self.dice:
                self.dice[die] = random.randint(1, 6)
            if self.fieldFlag == True:
                break
    
    def saveDices(self, saveList): # 선택한 주사위의 값을 리스트로 받아서 처리
        for i in saveList:
            for key, value in self.dice.items():
                if value == i:
                    self.save[key] = value
                    del(self.dice[key])
