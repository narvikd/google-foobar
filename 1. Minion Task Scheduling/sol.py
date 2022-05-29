def solution(data, n):
    return [i for i in data if data.count(i) <= n]


d = [5, 10, 15, 10, 7]
new_n = 1

print(solution(d, new_n))
