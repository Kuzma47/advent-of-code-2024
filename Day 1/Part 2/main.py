def solve(data: [str]) -> str:
    l1 = []
    l2 = dict()
    for line in data:
        a, b = map(int, line.split('   '))
        l1.append(a)
        if b not in l2:
            l2[b] = 0
        l2[b] += 1
    result = 0
    for n in l1:
        if n in l2:
            result += n * l2[n]
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
