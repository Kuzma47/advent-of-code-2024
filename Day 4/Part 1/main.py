MATRIX = []
WORD = 'XMAS'
WORD_REV = 'SAMX'


def check_word(word: str) -> int:
    if word == WORD:
        return 1
    if word == WORD_REV:
        return 1
    return 0


def solve() -> str:
    n = len(MATRIX)
    m = len(MATRIX[0])
    res = 0
    matrix_copy = MATRIX.copy()
    matrix = [[matrix_copy[i][j] for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            if i + 3 < n:
                word = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j]
                res += check_word(word)
            if j + 3 < m:
                word = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i][j + 3]
                res += check_word(word)
            if i + 3 < n and j + 3 < m:
                word = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3]
                res += check_word(word)
            if i + 3 < n and j - 3 >= 0:
                word = matrix[i][j] + matrix[i + 1][j - 1] + matrix[i + 2][j - 2] + matrix[i + 3][j - 3]
                res += check_word(word)
    return str(res)


if __name__ == '__main__':
    with open('input', 'r') as file:
        for l in file.readlines():
            MATRIX.append(l.rstrip())
        print(solve())
