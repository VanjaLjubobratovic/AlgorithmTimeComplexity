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
