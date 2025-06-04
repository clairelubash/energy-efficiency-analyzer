def process():
    for i in range(100):
        with open("file.txt", "w") as f:
            f.write(str(i))

process()