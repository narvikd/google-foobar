def solution(pegs):
    for i in range(1, pegs[1]):
        r = i
        for j, p in enumerate(pegs):
            try:
                new_index = pegs[j + 1]
            except IndexError:
                break
            r = new_index - (p + r)
            if r <= 0:
                break
        if r * 2 == i:
            return [i, 1]
        if r * 2 == i + 1:
            return [i * 3 + 1, 3]
        if r * 2 == i + 2:
            return [i * 3 + 2, 3]
    return [-1, -1]


print(solution([4, 30, 50]))
