def check(sequence: [int], rules) -> bool:
    for i in range(len(sequence)):
        n = sequence[i]
        for j in sequence[i+1:]:
            if j not in rules[n]:
                return False
    return True


def solve(data: [str]) -> str:
    result = 0
    i = 0
    rules = dict()
    while True:
        line = data[i].rstrip()
        if line == '':
            break
        x, y = map(int, line.split('|'))
        if x not in rules:
            rules[x] = set()
        rules[x].add(y)
        i += 1

    for line in data[i + 1:]:
        nums = list(map(int, line.split(',')))
        if check(nums, rules):
            result += nums[len(nums) // 2]
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
