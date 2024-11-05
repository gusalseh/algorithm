string = input()
string_2 = input()
length = len(string)
length_2 = len(string_2)
candidate=set()

for i in range(length+1):
    for j in range(i+1, length+1):
            candidate.add(string[i:j])

start = 0
count = 0

while start < length_2:
    for l in range(length_2, start, -1):
        if string_2[start:l] in candidate:
            start += l-start
            count += 1
            break

print(count)