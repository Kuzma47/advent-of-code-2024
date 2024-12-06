import time


class Guard:
    x: int
    y: int
    position: str

    def __init__(self, guard_x: int, guard_y: int, position: str):
        self.x = guard_x
        self.y = guard_y
        self.position = position
        self.turn_positions = set()

    def turn_90s(self) -> bool:
        if (self.x, self.y, self.position) in self.turn_positions:
            return True
        self.turn_positions.add((self.x, self.y, self.position))
        if self.position == '^':
            self.position = '>'
            return False
        if self.position == '>':
            self.position = 'v'
            return False
        if self.position == 'v':
            self.position = '<'
            return False
        if self.position == '<':
            self.position = '^'
            return False

    def is_reached_end(self) -> bool:
        return self.x == 0 or self.y == 0 or self.x == len(MATRIX[0]) - 1 or self.y == len(MATRIX) - 1

    def move(self) -> bool:
        if self.position == '^':
            next_y = self.y - 1
            if 0 <= next_y < len(MATRIX) and MATRIX[next_y][self.x] == '.':
                self.y = next_y
            elif MATRIX[next_y][self.x] == '#':
                return self.turn_90s()
        if self.position == '>':
            next_x = self.x + 1
            if 0 <= next_x < len(MATRIX[0]) and MATRIX[self.y][next_x] == '.':
                self.x = next_x
            elif MATRIX[self.y][next_x] == '#':
                return self.turn_90s()
        if self.position == 'v':
            next_y = self.y + 1
            if 0 <= next_y < len(MATRIX) and MATRIX[next_y][self.x] == '.':
                self.y = next_y
            elif MATRIX[next_y][self.x] == '#':
                return self.turn_90s()
        if self.position == '<':
            next_x = self.x - 1
            if 0 <= next_x < len(MATRIX[0]) and MATRIX[self.y][next_x] == '.':
                self.x = next_x
            elif MATRIX[self.y][next_x] == '#':
                return self.turn_90s()
        return False

MATRIX = []

def solve(start_x: int, start_y: int, position: str) -> str:
    start = time.time()
    possible_loops = 0
    progress = 0

    for barrier_y in range(len(MATRIX)):
        for barrier_x in range(len(MATRIX[0])):
            if barrier_x == start_x and barrier_y == start_y:
                continue
            progress += 1
            if progress % 1000 == 0:
                print(f'{progress}/{len(MATRIX) * len(MATRIX[0])}')
            if MATRIX[barrier_y][barrier_x] == '.':
                MATRIX[barrier_y][barrier_x] = '#'
                guard = Guard(start_x, start_y, position)
                while not guard.is_reached_end():
                    is_stuck = guard.move()
                    if is_stuck:
                        possible_loops += 1
                        break
                MATRIX[barrier_y][barrier_x] = '.'

    end = time.time()
    print(f'Elapsed: {end - start} seconds')
    return str(possible_loops)


if __name__ == '__main__':
    with open('input', 'r') as file:
        data = file.readlines()
        gx, gy = 0, 0
        position = ''
        for y in range(len(data)):
            line = list(data[y].rstrip())
            for x in range(len(line)):
                if line[x] != '#' and line[x] != '.':
                    position = line[x]
                    line[x] = '.'
                    gx, gy = x, y
            MATRIX.append(line)
        print(solve(gx, gy, position))
