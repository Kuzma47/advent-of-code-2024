import time


class Guard:
    x: int
    y: int
    position: str

    def __init__(self, guard_x: int, guard_y: int):
        self.x = guard_x
        self.y = guard_y
        self.position = MATRIX[self.y][self.x]
        UNIQ_POSITIONS.add((self.x, self.y))

    def turn_90s(self):
        if self.position == '^':
            self.position = '>'
            return
        if self.position == '>':
            self.position = 'v'
            return
        if self.position == 'v':
            self.position = '<'
            return
        if self.position == '<':
            self.position = '^'
            return

    def is_reached_end(self) -> bool:
        return self.x == len(MATRIX[0]) - 1 or self.y == len(MATRIX) - 1

    def move(self):
        if self.position == '^':
            next_y = self.y - 1
            if next_y < len(MATRIX) and MATRIX[next_y][self.x] == '.':
                self.y = next_y
            elif MATRIX[next_y][self.x] == '#':
                self.turn_90s()
                return
        if self.position == '>':
            next_x = self.x + 1
            if next_x < len(MATRIX[0]) and MATRIX[self.y][next_x] == '.':
                self.x = next_x
            elif MATRIX[self.y][next_x] == '#':
                self.turn_90s()
                return
        if self.position == 'v':
            next_y = self.y + 1
            if next_y < len(MATRIX) and MATRIX[next_y][self.x] == '.':
                self.y = next_y
            elif MATRIX[next_y][self.x] == '#':
                self.turn_90s()
                return
        if self.position == '<':
            next_x = self.x - 1
            if next_x < len(MATRIX[0]) and MATRIX[self.y][next_x] == '.':
                self.x = next_x
            elif MATRIX[self.y][next_x] == '#':
                self.turn_90s()
                return
        UNIQ_POSITIONS.add((self.x, self.y))


MATRIX = []
UNIQ_POSITIONS = set()


def solve(start_x: int, start_y: int) -> str:
    start = time.time()
    guard = Guard(start_x, start_y)
    while not guard.is_reached_end():
        guard.move()
    end = time.time()
    print(f'Elapsed: {end - start} seconds')
    return str(len(UNIQ_POSITIONS))

if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        gx, gy = 0, 0
        for y in range(len(data)):
            line = list(data[y].rstrip())
            for x in range(len(line)):
                if line[x] != '#' and line[x] != '.':
                    gx, gy = x, y
            MATRIX.append(line)
        print(solve(gx, gy))
