def fib(n: int, f: list) -> int:
    if(n > (len(f) - 1)):
        f.append(fib(n - 2, f) + fib(n - 1, f))
    return f[n]

print("Digite um valor: ")
n = int(input())
print(f'fib(5)= {fib(n, [0, 1])}')