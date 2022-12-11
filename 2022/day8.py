from typing import List
from util import readfile, Position


def visible_from_dir(grid: List[str], i: int, j: int, direction: str, height: int):
    next_i, next_j = Position.get_next_pos(i, j, direction)
    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid):
        return grid[next_i][next_j] < height and visible_from_dir(grid, next_i, next_j, direction, height)
    return True       
    

def day8_1(filepath: str) -> int:
    grid = readfile(filepath)
    count = len(grid) * 4 - 4 
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            for direction in Position.directions:
                if visible_from_dir(grid, i, j, direction, grid[i][j]):
                    count += 1
                    break 
    return count


def nb_visible_trees(grid: List[str], i: int, j: int, direction: str, height: int):
    next_i, next_j = Position.get_next_pos(i, j, direction)
    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid):
        if grid[next_i][next_j] >= height:
            return 1
        return 1 + nb_visible_trees(grid, next_i, next_j, direction, height)
    return 0


def day8_2(filepath: str) -> int:
    grid = readfile(filepath)
    max_score = 1
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            tree_score = 1
            for direction in Position.directions:
                tree_score *= nb_visible_trees(grid, i, j, direction, grid[i][j])
            max_score = max(max_score, tree_score)
    return max_score
    

if __name__ == "__main__":
    print(day8_1("inputs/day8.in"))
    print(day8_2("inputs/day8.in"))
