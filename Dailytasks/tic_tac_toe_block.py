#Given 2 positions on a Tic-Tac-Toe board, find the third position needed to block a win.
def blocking_spot(a, b):
    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in winning_lines:
        if a in line and b in line:
            for pos in line:
                if pos != a and pos != b:
                    return pos

print(blocking_spot(0, 1))
