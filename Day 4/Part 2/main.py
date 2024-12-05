MATRIX = []
WORDS = ['MAS', 'SAM']


def solve() -> str:
    n = len(MATRIX)
    m = len(MATRIX[0])
    res = 0
    matrix_copy = MATRIX.copy()
    matrix = [[matrix_copy[i][j] for j in range(n)] for i in range(m)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] != 'A':
                continue
            word1 = matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
            word2 = matrix[i + 1][j - 1] + matrix[i][j] + matrix[i - 1][j + 1]

            if word1 in WORDS and word2 in WORDS:
                res += 1

    return str(res)


if __name__ == '__main__':
    with open('input', 'r') as file:
        for l in file.readlines():
            MATRIX.append(l.rstrip())
        print(solve())
