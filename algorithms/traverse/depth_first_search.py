from data_structures.graph import GridMatrix


def grid_dfs(matrix: GridMatrix, x = 0, y = 0, count = 0, visited = []):
    """ Count no. of unique paths from top left to bottom right in GridMatrix.
    """
    neighbours = [(x, y-1), (x-1, y), (x, y+1), (x+1,y)]  # Up/left/down/right
    for i, j in neighbours:
        # Out of bounds (past top/left/bottom/right edges) OR blocked path OR already visited
        if i < 0 or j < 0 or i >= len(matrix.graph) or j >= len(matrix.graph) or matrix.graph[i][j] == 1 or (i, j) in visited:
            continue
        elif i == len(matrix.graph) - 1 and j == len(matrix.graph) - 1:  # Reached target
            return 1
        else:
            break
    
    visited.append((i, j))
    
    count += grid_dfs(matrix, x=(x-1), y=y, count=count, visited=visited)  # Up
    count += grid_dfs(matrix, x=x, y=(y-1), count=count, visited=visited)  # Left
    count += grid_dfs(matrix, x=(x+1), y=y, count=count, visited=visited)  # Down
    count += grid_dfs(matrix, x=x, y=(y+1), count=count, visited=visited)  # Right

    visited.pop((i, j))

    return count

if __name__ == '__main__':
    matrix = GridMatrix()
    matrix.rand_create(11)
    print(grid_dfs(matrix))
    