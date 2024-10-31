def solution(elements):
    N = len(elements)
    result = set()

    extended_elements = elements * 2

    for length in range(1, N + 1):
        for start in range(N):
            end = start + length
            subarray_sum = sum(extended_elements[start:end])
            result.add(subarray_sum)

    return len(result)
