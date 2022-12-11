from util import readfile
from pathlib import Path


def compute_dir_weights(filepath: str) -> dict:
    current_path = Path('/')
    directories = {'/' : 0}
    cnt = 0
    for line in readfile(filepath):
        if line == '' or line.startswith('$ cd'): 
            directories[str(current_path)] += cnt
            for i in range(len(current_path.parents)):
                directories[str(current_path.parents[i])] += cnt
            cnt = 0
            if line == '$ cd ..':
                current_path = current_path.parent
            elif line != '': 
                current_path = Path(current_path, line.split(' ')[-1])
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            directories[str(Path(current_path, line.split(' ')[-1]))] = 0
        else:
            cnt += int(line.split(' ')[0])
    return directories
    
    
def day7_1(filepath: str) -> int:
    dir_weights = compute_dir_weights(filepath)
    return sum([weight for weight in dir_weights.values() if weight < 100000])


def day7_2(filepath: str) -> int:
    dir_weights = compute_dir_weights(filepath)
    unused_space = 70000000 - dir_weights['/']
    needed_space = 30000000 - unused_space
    return min([weight for weight in dir_weights.values() if weight >= needed_space])


if __name__ == "__main__":
    print(day7_1("inputs/day7.in"))
    print(day7_2("inputs/day7.in"))
