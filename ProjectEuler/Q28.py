import numpy as np
import tqdm

max_side_length = 7

spiral = np.zeros((max_side_length, max_side_length))
direction_indicator = 3
# 0 mod 4 is right, 1 mod 4 is down, 2 mod 4 is left, 3 mod 4 is up
square_size = 0
x, y = max_side_length // 2, max_side_length // 2
direction_lookup = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

def in_small_square(x, y, s):
    not_oob = x < max_side_length and y < max_side_length
    return not_oob and abs(x - max_side_length // 2) < s and abs(y - max_side_length // 2) < s and x >= 0 and y >= 0

for i in tqdm.trange(1, 26):
    spiral[x][y] = i
    dx, dy = direction_lookup.get(direction_indicator % 4)
    if not in_small_square(x + dx, y + dy, square_size):
        direction_indicator += 1
        if direction_indicator % 4 in [0, 2]:
            square_size += 1
        dx, dy = direction_lookup.get(direction_indicator % 4)
    x += dx
    y += dy

print(spiral)
