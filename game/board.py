from config import boardinfo
LEN = 3

class Board:
    def __init__(self, initBoard=None, move=None):
        if initBoard is None:
            self.board = [[0] * 3 for _ in range(LEN)]
        else:
            """
                TODO:
                    近いうちに局面を指定されたときの実装をする
            """
            raise Exception("Unimplemented!!!")
    
    def __setitem__(self, keys, value):
        f, n = keys
        self.board[f][n] = value

    def __getitem__(self, keys):
        f, n = keys
        return self.board[f][n]
    
    def judge(self, a, b, c):
        if self[a] != 0 and self[a] == self[b] and self[b] == self[c]:
            return self[a]
        else:
            return 0
    
    def actlist(self):
        """
            移動可能な場所を探す
        """
        return [
            i for i in range(LEN**2) if self[divmod(i, 3)] == 0
        ]
    
    def show(self):
        for i in range(3):
            for j in range(3):
                print(boardinfo[self[i, j]], end=' ')
            print()
        print()


if __name__ == "__main__":
    b = Board()
    print(b.board)
    b[0, 0] = 1
    print(b.board)
    print(b[0, 0])
    for i in range(3):
        b[i, i] = 1
    val = [
        (i, i) for i in range(3)
    ]
    print(b.board)
    print(b.judge(*val))
    print(b.actlist())