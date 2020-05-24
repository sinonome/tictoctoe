from board import Board
from game import TicTocToe
from agent import RandomAgent, Human
from config import FIRST, LOSE, ENDGAME, boardinfo
import time
from view import viewBoard

def main(view=False, result=False):
    player1 = Human()
    player2 = RandomAgent()
    
    env = TicTocToe()
    state = env.setGame()
    done = False
    turn = FIRST
    
    try:
        while not done:
            if view:
                viewBoard(state)
            if turn == FIRST:
                action = player1.action(state)
            else:
                action = player2.action(state)

            state, info = env.step(divmod(action, 3))
            done = (info == ENDGAME)
            turn *= -1
            time.sleep(0.1)

        if env.winner:
            name = "player1" if env.winner == FIRST else "player2"
            print(name + " win!")
        else:
            print("引き分けです")
        if result:
            print("--- result ----------------")
            state.show()
            

    except KeyboardInterrupt:
        print("終了します。")
    except:
        import traceback; traceback.print_exc()
        name = "player1" if turn != FIRST else "player2"
        print(name + " win!")


if __name__ == "__main__":
    main(False, True)