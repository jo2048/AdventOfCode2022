from util import readfile


def load_monkey_roles(filepath: str) -> dict:
    lines = readfile(filepath)
    roles = dict()
    for line in lines:
        monkey, role = line.split(': ')
        if role.isdigit():
            roles[monkey] = int(role)
        else:
            op = role[5]
            roles[monkey] = (role[5], *role.split(role[4:7]))
    return roles


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


######################### PART 1 #########################
def eval_monkey(roles: dict, monkey: str) -> int:
    if type(roles[monkey]) is int:
        return roles[monkey]
    else:
        op, monkey1, monkey2 = roles[monkey]
        m1 = eval_monkey(roles, monkey1)
        m2 = eval_monkey(roles, monkey2)
        return OPERATIONS[op](m1, m2)
        

def day21_1(filepath: str) -> int:
    roles = load_monkey_roles(filepath)
    return eval_monkey(roles, 'root')


######################### PART 2 #########################
def solve(roles: dict, monkey: str) -> int:
    if monkey == 'humn':
        return (None, None, None)
    if type(roles[monkey]) is int:
        return roles[monkey]
    else:
        op, monkey1, monkey2 = roles[monkey]
        m1 = solve(roles, monkey1)
        m2 = solve(roles, monkey2)
        if type(m1) is int and type(m2) is int:
            roles[monkey] = OPERATIONS[op](m1, m2)
        elif type(m1) is int:
            roles[monkey] = (op, m1, monkey2)
        elif type(m2) is int:
            roles[monkey] = (op, monkey1, m2)
    return roles[monkey]


def find_x(roles, monkey, val):
    op, m1, m2 = roles[monkey]
    nb, next_monkey = m1, m2
    if type(m2) is int:
        nb, next_monkey = m2, m1
    if op == '+':
        val -= nb
    elif op == '-':
        if next_monkey == m2:
            val = -val
        val += nb
    elif op == '*':
        val //= nb
    else:
        if next_monkey == m2:
            val = 1/val
        val *= nb
    if next_monkey == 'humn':
        return val
    return find_x(roles, next_monkey, val)


def day21_2(filepath: str) -> int:
    roles = load_monkey_roles(filepath)
    op, monkey1, monkey2 = roles['root']
    m1 = solve(roles, monkey1)
    m2 = solve(roles, monkey2)
    val, monkey = m1, monkey2
    if type(m1) is not int:
        val, monkey = m2, monkey1
    return find_x(roles, monkey, val)


if __name__ == "__main__":
    print(day21_1("inputs/day21.in"))
    print(day21_2("inputs/day21.in"))
