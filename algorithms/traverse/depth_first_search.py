from data_structures.graph import GridMatrix


def grid_dfs(matrix: GridMatrix, r = 0, c = 0, visited = None):
    """ Count no. of unique paths from top left to bottom right in GridMatrix (a square grid).
    """
    if visited is None:
        visited = []

    count = 0
    # Out of bounds (past left/up/right/bottom edges) OR blocked path OR already visited
    if r < 0 or c < 0 or r >= len(matrix.graph) or c >= len(matrix.graph) or matrix.graph[r][c] == 1 or (r, c) in visited:
        return 0
    elif r == len(matrix.graph) - 1 and c == len(matrix.graph) - 1:  # Reached target
        return 1
    else:
        visited.append((r, c))

        neighbours = [(r, c-1), (r-1, c), (r, c+1), (r+1,c)]  # Left, Up, Right, Down
        for i, j in neighbours:
            count += grid_dfs(matrix, r=i, c=j, visited=visited)

        visited.pop()

    return count

if __name__ == '__main__':
    matrix = GridMatrix()
    matrix.graph = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    print(grid_dfs(matrix))
    