# GAME STATE
STANDBY =  0
NOWGAME =  1
ENDGAME = -1

FIRST =  1
LOSE  = -1

# Judge Info
LINE = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]

# Agent Mode
RANDOM = 0
HUMAN  = 1

MARU = 'o'
BATU = 'x'
NOTH = '.'

boardinfo = {
    -1 : BATU,
     0 : NOTH,
     1 : MARU,
}