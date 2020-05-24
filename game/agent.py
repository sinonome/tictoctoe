import numpy as np

class Agent:
    def action(self, state):
        raise Exception('not defined')


class RandomAgent(Agent):
    # name = 'name'
    def __init__(self, RandomState=None):
        self.rand = np.random.RandomState(RandomState)
    
    def action(self, state):
        return self.rand.choice(state.actlist())

if __name__ == "__main__":
    from board import Board
    
    a = RandomAgent()
    for i in range(10):
        print(a.action(Board()))

class Human(Agent):
    def action(self, state):
        print("--- now ----------------")
        state.show()
        actlst = state.actlist()
        actnum = [
            divmod(i, 3) for i in actlst
        ]
        print("行動を選んで下さい")
        print(*actnum)
        while True:
            try:
                a, b = map(int, input(">> ").split())
                act = a * 3 + b
                if act in actlst and self.canmove(a, b):
                    return act
                else:
                    raise Exception("can't move!")
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                print("与えられたパラメータが不正です")

    def canmove(self, a, b):
        return (
            0 <= a and a < 3 and
            b <= b and b < 3
        )