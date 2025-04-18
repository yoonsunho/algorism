def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

print(fibo2(10)) # 55

# 0 1 1 2 3 5 8 13 21 34 55

def fibo(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

print(fibo(10))