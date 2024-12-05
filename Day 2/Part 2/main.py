def sign(n: int) -> int:
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def is_safe(seq: [int], attempt: int = 0) -> bool:
    previous_level = seq[0]
    s = sign(previous_level - seq[1])
    i = 0
    for level in seq[1:]:
        i += 1
        diff = s * (previous_level - level)
        previous_level = level
        if 1 <= diff <= 3:
            continue
        else:
            if attempt < 1:
                results = []
                for i in range(len(seq)):
                    seq_copy = seq.copy()
                    seq_copy.pop(i)
                    results.append(is_safe(seq_copy, 1))
                return True in results
            return False
    return True


def solve(data: [str]) -> str:
    result = 0
    for line in data:
        levels = list(map(int, line.split(' ')))
        if is_safe(levels):
            result += 1

    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        print(solve(data))
