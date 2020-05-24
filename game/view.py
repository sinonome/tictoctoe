from config import boardinfo

def viewBoard(state, st = 'now'):
    print("--- "+st+" ----------------")
    for i in range(3):
        for j in range(3):
            print(boardinfo[state[i, j]], end=' ')
        print()
    print()