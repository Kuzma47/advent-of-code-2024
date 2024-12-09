import itertools


def do_math_left_to_right(expression: str, goal: int) -> int:
    pieces = []

    i = 0
    for c in expression:
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            try:
                pieces[i] += c
            except IndexError:
                pieces.append(c)
        elif c in {'+', '|', '*'}:
            i += 1
            pieces.append(c)

    last_piece = pieces.pop(0)
    result = 0
    for piece in pieces:
        to_eval = f'{last_piece}{piece}'
        if '|' in to_eval:
            result = int(''.join(to_eval.split('|')))
        else:
            result = eval(to_eval)
        if result > goal:
            return 0
        last_piece = str(result)
    return result


def solve(data: [str]) -> str:
    result = 0
    for line in data:
        test_value, nums = line.split(': ')
        test_value = int(test_value)

        if int(nums.replace(' ', '')) < test_value:
            continue

        nums = list(map(int, nums.split(' ')))
        for operators in list(itertools.product('+*|', repeat=len(nums)-1)):
            expr = ''
            for i in range(len(operators)):
                expr += str(nums[i]) + str(operators[i])
            expr += str(nums[-1])
            if do_math_left_to_right(expr, test_value) == test_value:
                result += test_value
                break

    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
