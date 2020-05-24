from board import Board
from config import STANDBY, NOWGAME, ENDGAME, FIRST, LOSE, LINE

class TicTocToe:
    def __init__(self):
        self.board   = None
        self.next    = None
        self.state   = STANDBY    
        self.winner  = None
        self.number  = None

    def setGame(self):
        """
            ゲーム初期化を行う
        """
        self.board  = Board()
        self.next   = FIRST
        self.state  = NOWGAME
        self.winner = None
        self.number = 0
        return self.board
    
    def step(self, action):
        """
            ゲームを1つ進める
        """
        if self.state != NOWGAME:
            if self.state == STANDBY:
                raise Exception("game not start! plearse initialize game.")
            else:
                raise Exception("game has already finish!")

        info = self.state

        if self.next == FIRST:
            if self.board[action] != 0:
                raise Exception("this mass already exists!")
            self.board[action] = FIRST
            self.next = LOSE

        else:
            self.board[action] = LOSE
            self.next = FIRST
        
        self.number += 1
        res = self.judge()

        if res:
            self.state  = ENDGAME
            self.winner = res
            info = ENDGAME
        elif self.number >= 9:
            self.state = ENDGAME
            self.winner = 0
            info = ENDGAME

        return self.board, info

    def judge(self):
        """
            揃っているラインがあるかを判定し、あればどちらが勝っているかを出力
        """
        for coors in LINE:
            res = self.board.judge(*coors)
            if res != 0:
                return res
        
        return 0