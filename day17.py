from util.files import *
from util.runner import *
import math
import time

TESTING = False

lines = GetLines(17, TESTING)

X_START_OFFSET = 2
Y_START_OFFSET = 4

def parse():
    jet_directions = []
    for line in lines:
        for c in line:
            if c == '<':
                jet_directions.append(-1)
            else:
                jet_directions.append(1)
    solid_squares = set([(x,0) for x in range(7)])
    return jet_directions, solid_squares

def spawn_rock(tower_height, pattern):
  x, y = (X_START_OFFSET, tower_height + Y_START_OFFSET)

  if pattern == 0:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 3, y)
    ])
  elif pattern == 1:
    return set([
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1),
      (x + 2, y + 1),
      (x + 1, y + 2)
    ])
  elif pattern == 2:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 2, y + 1),
      (x + 2, y + 2)
    ])
  elif pattern == 3:
    return set([
      (x, y),
      (x, y + 1),
      (x, y + 2),
      (x, y + 3)
    ])
  elif pattern == 4:
    return set([
      (x, y),
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1)
    ])

def should_fall(rock, solid_squares):
  for square in rock:
    x,y = square

    if (x, y - 1) in solid_squares:
      return False

  return True

def should_push(rock, direction, solid_squares):
  for square in rock:
    x,y = square

    if direction == -1 and x - 1 < 0:
      return False
    
    if direction == 1 and x + 1 > 6:
      return False
    
    if (x + direction, y) in solid_squares:
      return False

  return True

def push(rock, direction):
  return set([(x + direction, y) for x,y in rock])

def fall(rock):
  return set([(x, y - 1) for x,y in rock])

def come_to_rest(rock, solid_squares, placed_rocks):
  max_y = 0

  for square in rock:
    _,y = square
    solid_squares.add(square)
    max_y = max(max_y, y)

  placed_rocks.append(rock)
  
  return (max_y, rock)


def part1():
    jet_directions, solid_squares = parse()
    next_jet = 0
    next_rock = 0
    tower_height = 0
    ROCKS_TO_FALL = 2022

    r = 0

    while r < ROCKS_TO_FALL:
        rock = spawn_rock(tower_height, next_rock)
        while True:
            direction = jet_directions[next_jet]
            next_jet = (next_jet + 1) % len(jet_directions)

            if should_push(rock, direction, solid_squares):
                rock = push(rock, direction)

            if should_fall(rock, solid_squares):
                rock = fall(rock)
            else:
                break
        max_y, rock = come_to_rest(rock, solid_squares, [])
        tower_height = max(tower_height, max_y)
        next_rock = (next_rock + 1) % 5
        r += 1
    return tower_height

def part2():
    jet_directions, solid_squares = parse()
    placed_rocks = []
    next_jet = 0
    next_rock = 0
    tower_height = 0
    seen_states = {}
    cycle_found = False
    ROCKS_TO_FALL = 1000000000000
    N_ROCKS_IN_STATE = 30 # MAGIC NUMBER

    r = 0

    while r < ROCKS_TO_FALL:
      if not cycle_found:
        last_n_rocks = list(map(
          lambda rock: frozenset([(x, y - tower_height) for x,y in rock]),
          placed_rocks[-N_ROCKS_IN_STATE:]
        ))

        start_state = frozenset([
          next_jet,
          next_rock,
          frozenset(last_n_rocks)
        ])

        if start_state in seen_states:
          cycle_found = True
          r0, height0 = seen_states[start_state]

          cycle_length = r - r0
          height_per_cycle = tower_height - height0
          remaining_rocks = ROCKS_TO_FALL - r0
          num_cyles = math.floor(remaining_rocks / cycle_length)

          r = r0 + (cycle_length * num_cyles)
          tower_height = height0 + (height_per_cycle * num_cyles)

          for rock in last_n_rocks:
            for x,y in rock:
              solid_squares.add((x, y + tower_height))

        else:
          seen_states[start_state] = (r, tower_height)

      rock = spawn_rock(tower_height, next_rock)

      while True:
        direction = jet_directions[next_jet]
        next_jet = (next_jet + 1) % len(jet_directions)

        if should_push(rock, direction, solid_squares):
          rock = push(rock, direction)

        if should_fall(rock, solid_squares):
          rock = fall(rock)
        else:
          break
      
      max_y, rock = come_to_rest(rock, solid_squares, placed_rocks)
      tower_height = max(tower_height, max_y)
      next_rock = (next_rock + 1) % 5
      r += 1

    return tower_height


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(17, ans1, ans2, time1, time2)
