def fib_non_dynamic(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return fib_non_dynamic(n - 1) + fib_non_dynamic(n - 2)

def fib_non_dynamic_list(n):
    fibo_vals = []
    for i in range(n):
        fibo_vals.append(fib_non_dynamic(i))
    return fibo_vals