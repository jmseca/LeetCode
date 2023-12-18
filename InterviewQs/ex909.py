def snakesAndLadders( board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    cols, rows = len(board[0]), len(board)
    n2 = cols*rows
    
    def val_to_rc(n):
        n -= 1  # Adjust n to start from 0
        row, col = divmod(n, cols)
        if row % 2 == 1:
            # Odd row, count from right to left
            col = cols - 1 - col
        # Calculate the actual row based on the board starting from the bottom
        row = rows - 1 - row
        return row, col
    

    # Step 1 - Build the graph
    graph = {}
    for curr in range(1,n2+1):
        graph[curr] = set()
        max_pos = min(curr + 6, n2)
        for next in range(curr + 1, max_pos + 1):
            r,c = val_to_rc(next)
            if board[r][c] == -1:
                graph[curr].add(next)
            else:
                print(f"YOOOO, r={r}, c={c}")
                print("key =",curr,"  ",graph[curr],board[r][c])
                graph[curr].add(board[r][c])

    # Step 2 - Find shortest path
    to_see = [[1,0]] # [curr, cost_till_curr]
    seen = {}
    #found = False
    possibilities = []
    while to_see: #and not(found):
        curr,cost = to_see.pop()
        if curr == n2:
            #found = True
            possibilities += [cost]
        else:
            for next in graph[curr]:
                if next not in seen or seen[next]>cost+1:
                    seen[next] = cost+1
                    to_see += [[next, cost+1]]
            #to_see = sorted(to_see, key = lambda x:x[1])


    #return found
    print(possibilities)
    #print(graph)
    return -1 if not(possibilities) else min(possibilities)

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(board))