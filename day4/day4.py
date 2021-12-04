with open('input.txt', 'r') as f:
    strlines = f.readlines()

def call_num(board, x):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == x:
                board[i][j] = -1
    return board

def check_board(board):
    for i in range(len(board)):
        horz = True
        for j in range(len(board[i])):
            if board[i][j] != -1:
                horz = False
                break
        if horz:
            return True
    for j in range(len(board[0])):
        vert = True
        for i in range(len(board)):
            if board[i][j] != -1:
                vert = False
                break
        if vert:
            return True
    return False

def score_board(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                score += board[i][j]
    return score

boards = []
for i in range(2, len(strlines), 6):
    board = [[0]*5 for _ in range(5)]
    for j in range(i, i+5):
        bline = strlines[j].split()
        for k in range(5):
            board[j-i][k] = int(bline[k])
    boards.append(board)

nums = strlines[0].split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(nums)

found = False
for num in nums:
    for i in range(len(boards)):
        boards[i] = call_num(boards[i], num)
        if check_board(boards[i]):
            print(score_board(boards[i])*num)
            found = True
            break
    if found:
        break

wbscore = 0
lastj = 0

for i in range(len(boards)):
    for j in range(len(nums)):
        num = nums[j]
        boards[i] = call_num(boards[i], num)
        if check_board(boards[i]):
            score = score_board(boards[i])*num
            if j > lastj:
                wbscore = score
                lastj = j
            break

print(wbscore)
