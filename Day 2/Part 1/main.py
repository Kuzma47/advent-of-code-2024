def sign(n: int) -> int:
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def solve(data: [str]) -> str:
    result = 0
    for line in data:
        levels = list(map(int, line.split(' ')))
        result += 1
        previous_level = levels[0]
        s = sign(previous_level - levels[1])
        for level in levels[1:]:
            diff = s * (previous_level - level)
            previous_level = level
            if 1 <= diff <= 3:
                continue
            else:
                result -= 1
                break
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
