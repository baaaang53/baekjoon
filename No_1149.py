
N = int(input())
grid = []

# generate grid
for i in range(0,N) :
    inp = input().split(" ")
    inp = [int(j) for j in inp]
    grid.append(inp)

for i in range(N-2, -1, -1) :
    for color in range(0, 3):
        k = grid[i][color] + grid[i + 1][(color + 1) % 3]
        if (k > grid[i][color] + grid[i + 1][(color + 2) % 3]):
            k = grid[i][color] + grid[i + 1][(color + 2) % 3]
        grid[i][color] = k


print(min(grid[0][0], grid[0][1], grid[0][2]))

