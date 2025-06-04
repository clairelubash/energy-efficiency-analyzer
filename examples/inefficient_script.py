import io

def recurse(n):
    if n == 0:
        return 0
    return recurse(n - 1)

def process():
    for i in range(10):
        # Simulate I/O without actual disk write
        fake_file = io.StringIO()
        fake_file.write(str(i))
        fake_file.close()
    recurse(5)

process()
