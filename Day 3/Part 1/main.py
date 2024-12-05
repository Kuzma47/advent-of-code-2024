import re


def solve(data: str) -> str:
    result = 0
    multipliers = re.findall(r'mul\(\d+,\d+\)', data)
    print(len(multipliers))
    for mul in multipliers:
        nums = list(map(int, mul[4:-1].split(',')))
        result += nums[0] * nums[1]
    return str(result)


if __name__ == '__main__':
    with open('input', 'r') as file:
        raw_data = file.readlines()
        data = ' '.join(raw_data)
        print(solve(data))
