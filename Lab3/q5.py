def count_islands(grid):
    def dfs(r, c):
        if r < 0 or r >= 10 or c < 0 or c >= 10 or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

grid = [
    list("1100000111"),
    list("1000000111"),
    list("0000000111"),
    list("0010001000"),
    list("0000011100"),
    list("0000111110"),
    list("0001111111"),
    list("1000111110"),
    list("1100011100"),
    list("1110001000")
]

print(count_islands(grid))

