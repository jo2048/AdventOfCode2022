from typing import Tuple


def readfile(filepath: str, keep_last_empty_line: bool=False) -> list:
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()
    if not keep_last_empty_line and lines[-1] == '\n':
        lines.pop()
    return [l.strip('\n') for l in lines]
    

class Position:
    directions = ['L', 'U', 'R', 'D']

    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y
    
    def apply_move(self, direction: str):
        self.x, self.y = Position.get_next_pos(self.x, self.y, direction)

    def get_next_pos(x: int, y: int, direction: str) -> Tuple[int]:
        if direction == 'L':
            return x, y - 1
        elif direction == 'R':
            return x, y + 1
        elif direction == 'U':
            return x - 1, y
        else:   
            return x + 1, y
