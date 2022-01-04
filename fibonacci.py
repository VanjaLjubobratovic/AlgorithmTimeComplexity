MAX = 10000000

def fib_non_dynamic(n):
    if n <= 1:
        return 1
    return fib_non_dynamic(n - 1) + fib_non_dynamic(n - 2)

def fib_non_dynamic_list(n):
    fibo_vals = []
    for i in range(n):
        fibo_vals.append(fib_non_dynamic(i))
    return fibo_vals

def fib_dynamic(n, list):
    arr = [1, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    if list == True:
        return arr
    else:
        return arr[-1]

f = [0] * MAX
def fib_optimized(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]
    if (f[n]):
        return f[n]
    if n & 1:
        k = (n + 1) // 2
    else:
        k = n // 2
    
    if (n & 1):
        f[n] = (fib_optimized(k) * fib_optimized(k) + fib_optimized(k - 1) * fib_optimized(k - 1))
    else:
        f[n] = (2 * fib_optimized(k - 1) + fib_optimized(k)) * fib_optimized(k)
    return f[n]

