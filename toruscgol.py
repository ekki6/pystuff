SIZE = 20

#grid is SIZE x SIZE with padding of zeros
#treat as torus
#this one 20x20
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


#def local_sum(r,c):
#    acc = 0
#    acc += grid[r-1][c-1]
#    acc += grid[r-1][c]
#    acc += grid[r-1][c+1]
#    acc += grid[r][c-1]
#    acc += grid[r][c+1]
#    acc += grid[r+1][c-1]
#    acc += grid[r+1][c]
#    acc += grid[r+1][c+1]
#    return acc


def local_sum(r,c):
    acc = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            acc += grid[(r+dr)%SIZE][(c+dc)%SIZE]
    return acc


while True:

# modified to remove padding
#    for row in grid[1:-1]:
#        print(" ".join(map(str, row[1:-1])))
    
# modified to remove padding and use symbols
    for row in grid:
        print(" ".join("O" if x else "-" for x in row[1:-1]))
    
#    for row in grid:
#        print(" ".join(map(str, row)))
    
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
