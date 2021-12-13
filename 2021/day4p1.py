data = data.split("\r\n\r\n")
nums = list(map(int, data[0].split(",")))

boards = []
for k in data[1:]:
    boards.append([])
    for j in k.splitlines():
        boards[-1].append(list(map(int, j.split())))

for num in nums:
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = None
        if any(all(x == None for x in row) for row in board) or any(all(row[i] == None for row in board) for i in range(len(board[0]))):
            print(sum(x or 0 for row in board for x in row) * num)
            exit(0)
