from typing import List
from util import readfile, Position, Grid


def visible_from_dir(grid: Grid, p: Position, direction: str, height: int):
    next_pos = p.get_next_pos(direction)
    if grid.within_bounds(next_pos):
        return grid.get_value_at(next_pos) < height and visible_from_dir(grid, next_pos, direction, height)
    return True       
    

def day8_1(filepath: str) -> int:
    grid = Grid.init_from_str_list(readfile(filepath))
    count = grid.width * 4 - 4 
    
    for i in range(1, grid.height - 1):
        for j in range(1, grid.width - 1):
            p = Position(i, j)
            for direction in Position.directions:
                if visible_from_dir(grid, p, direction, grid.get_value_at(p)):
                    count += 1
                    break 
    return count


def nb_visible_trees(grid: Grid, p: Position, direction: str, height: int):
    next_pos = p.get_next_pos(direction)
    if grid.within_bounds(next_pos):
        if grid.get_value_at(next_pos) >= height:
            return 1
        return 1 + nb_visible_trees(grid, next_pos, direction, height)
    return 0


def day8_2(filepath: str) -> int:
    grid = Grid.init_from_str_list(readfile(filepath))
    max_score = 1
    
    for i in range(1, grid.height - 1):
        for j in range(1, grid.width - 1):
            tree_score = 1
            p = Position(i, j)
            for direction in Position.directions:
                tree_score *= nb_visible_trees(grid, p, direction, grid.get_value_at(p))
            max_score = max(max_score, tree_score)
    return max_score
    

if __name__ == "__main__":
    print(day8_1("inputs/day8.in"))
    print(day8_2("inputs/day8.in"))
