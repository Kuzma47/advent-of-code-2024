def solve(data: [str]) -> str:
    l1 = []
    l2 = []
    for line in data:
        a, b = map(int, line.split('   '))
        l1.append(a)
        l2.append(b)
    l1 = sorted(l1)
    l2 = sorted(l2)
    result = 0
    for a, b in zip(l1, l2):
        result += abs(a - b)
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
