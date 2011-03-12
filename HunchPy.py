def fib(n):
    alpha = 0
    beta = 1
    for i in range(n):
        alpha , beta = beta , alpha + beta
    return alpha
