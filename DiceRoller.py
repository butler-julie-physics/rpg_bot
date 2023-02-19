# Dice Roller

import numpy as np

class DiceRoller:
    # D3, D4, D5, D6, D7, D8, D10, D%10, D12, D14, D16, D20, D24, and D30. 
    def __init__(self):
        pass
    
    def roll(self,d,mod=0,num=1):
        result = mod
        for i in range(num):
            result = result + np.random.randint(1,d)
        return result

    def d2(self, mod=0, num=1):
        return self.roll(2, mod, num)

    def d3(self, mod=0, num=1):
        return self.roll(3, mod, num)

    def d4(self, mod=0, num=1):
        return self.roll(4, mod, num)

    def d5(self, mod=0, num=1):
        return self.roll(5, mod, num)

    def d6(self, mod=0, num=1):
        return self.roll(6, mod, num)

    def d7(self, mod=0, num=1):
        return self.roll(7, mod, num)

    def d8(self, mod=0, num=1):
        return self.roll(8, mod, num)

    def d10(self, mod=0, num=1):
        return self.roll(10, mod, num)

    def d12(self, mod=0, num=1):
        return self.roll(12, mod, num)

    def d14(self, mod=0, num=1):
        return self.roll(14, mod, num)

    def d16(self, mod=0, num=1):
        return self.roll(16, mod, num)

    def d20(self, mod=0, num=1):
        return self.roll(20, mod, num)

    def d24(self, mod=0, num=1):
        return self.roll(24, mod, num)

    def d30(self, mod=0, num=1):
        return self.roll(30, mod, num)

    def d100(self, mod=0, num=1):
        return self.roll(100, mod, num)
    
    def d_any (self, d=1, mod=0, num=1):
        return self.roll(d, mod, num)


    
