N, L = map(int, input().split())
hole = [tuple(map(int, input().split())) for _ in range(N)]

hole.sort()

total_number = 0
position = 0

for start, end in hole:
    if position < start:
        position = start

    distance = end - position
    if distance > 0:
        needed_number = (distance + L - 1) // L
        total_number += needed_number
        position += needed_number * L

print(total_number)