def recurse(n):
    if n == 0:
        return 0
    return recurse(n - 1)

def process():
    for i in range(10):
        with open("file.txt", "w") as f:
            f.write(str(i))
    recurse(5)

process()