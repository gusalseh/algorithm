T = int(input())
k = int(input())
coins = [tuple(map(int, input().split())) for _ in range(k)]

func = [0] * (T + 1)
func[0] = 1

for p, n in coins:
    new_func = [0] * (T + 1)

    for amount in range(T + 1):
        count = func[amount]
        if count == 0:
            continue

        for used in range(n + 1):
            new_amount = amount + used * p
            if new_amount > T:
                break
            new_func[new_amount] += count

    func = new_func

print(func[T])