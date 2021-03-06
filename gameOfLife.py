import cellularAutomaton


class gameOfLife(cellularAutomaton.cellularAutomaton):
    @staticmethod
    def state0(self, x, y):
        count = self.countAround(x, y, 1)
        if count == 3:
            return 1
        else:
            return 0
    @staticmethod
    def state1(self, x, y):
        count = self.countAround(x, y, 1)
        if count == 2 or count == 3:
            return 1
        else:
            return 0

    def __init__(self, sizeX, sizeY,
                 looping=True):
        super().__init__(sizeX, sizeY, 2, 0, looping)
        self.transitionFunctionList[0] = self.state0
        self.transitionFunctionList[1] = self.state1
