SIZE = 20

#grid = [
#    ["1" if (r + c) % 2 == 0 else "0" for c in range(SIZE)]
#    for r in range(SIZE)
#]

grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


def local_sum(r,c):
    acc = 0
    if r > 0 and c > 0:
        acc += grid[r-1][c-1]
    if r > 0:
        acc += grid[r-1][c]
    if r > 0 and c < (SIZE - 1):
        acc += grid[r-1][c+1]
    if c > 0:
        acc += grid[r][c-1]
    if c < (SIZE - 1):
        acc += grid[r][c+1]
    if r < (SIZE - 1) and c > 0:
        acc += grid[r+1][c-1]
    if r < (SIZE - 1):
        acc += grid[r+1][c]
    if r < (SIZE - 1) and c < (SIZE - 1):
        acc += grid[r+1][c+1]
    return acc

while True:

    for row in grid:
        print(" ".join(map(str, row)))
    
    key = input("\n<Enter> for next generation, q to quit: ")

    grid2 = [
        [0 for c in range(SIZE)]
        for r in range(SIZE)
    ]

    if key.lower() == "q":
        break

    # find births, deaths (and survives)
    for r in range(SIZE):
        for c in range(SIZE):
            lsum = local_sum(r,c)
            if grid[r][c] == 1:
                if ((lsum == 2) or (lsum == 3)):
                    grid2[r][c] = 1
                else:
                    grid2[r][c] = 0
            if grid[r][c] == 0:
                if lsum == 3:
                    grid2[r][c] = 1
                else:
                    grid2[r][c] = 0
    grid = grid2
                    

    print()      # blank line between generations
