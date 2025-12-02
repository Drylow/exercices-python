def fibonacci(n):
    seq = [0, 1]
    while seq[-1] < n:
        seq.append(seq[-1] + seq[-2])
    return seq
print(fibonacci(100))

def generate_fibonacci(n):
    a, b = 0, 1
    yield a
    yield b
    while b < n:
        a, b = b, a + b
        yield b
print(list(generate_fibonacci(10)))