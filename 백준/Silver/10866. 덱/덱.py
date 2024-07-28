N = int(input())
input_list = []
deque = []

for _ in range(N):
    order = str(input())
    input_list.append(order)

for order in input_list:
    if "push_front" in order or "push_back" in order:
        real_order = order.split()[0]
        order_num = order.split()[1]
        if real_order == "push_front":
            deque.insert(0,int(order_num))
        elif real_order == "push_back":
            deque.append(int(order_num))
    elif order == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif order == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
