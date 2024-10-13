R, C = map(int, input().split())
puzzle = [input() for _ in range(R)]
words = []

for row in puzzle:
    word_in_row = row.split('#')
    for word in word_in_row:
        if len(word) >= 2:
            words.append(word)

for col in range(C):
    column_string = ''
    for row in range(R):
        column_string += puzzle[row][col]
    word_in_col = column_string.split('#')
    for word in word_in_col:
        if len(word) >= 2:
            words.append(word)

words.sort()
print(words[0])