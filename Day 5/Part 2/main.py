def correct_sequence(sequence: [int], rules) -> [int]:
    corrected = []
    taken = set()
    while len(corrected) != len(sequence):
        for i in range(len(sequence)):
            if i in taken:
                continue
            n = sequence[i]
            is_correct = True
            for j in range(len(sequence)):
                if j == i or j in taken:
                    continue
                checking_n = sequence[j]
                if checking_n not in rules[n]:
                    is_correct = False
                    break
            if is_correct:
                corrected.append(n)
                taken.add(i)
    return corrected


def check(sequence: [int], rules) -> bool:
    for i in range(len(sequence)):
        n = sequence[i]
        for checking_n in sequence[i+1:]:
            if checking_n not in rules[n]:
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
        if not check(nums, rules):
            corrected = correct_sequence(nums, rules)
            result += corrected[len(corrected) // 2]
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
