def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    pos = [i for i in xs if i > 0]
    neg = [i for i in xs if i < 0]

    if len(neg) % 2 != 0:
        neg.remove(max(neg))

    if len(pos) == 0 and len(neg) == 0:
        return str(0)

    product = reduce(lambda x, y: x * y, pos + neg)

    return str(product)


xs1 = [-2, -3, 4, -5]

print(solution(xs1))
