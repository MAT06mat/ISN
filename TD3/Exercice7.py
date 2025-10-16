def u(n):
    res = 1
    for i in range(n):
        res = 1 + 1 / (res)
    return res


print(u(5000))
