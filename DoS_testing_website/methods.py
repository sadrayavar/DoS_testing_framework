import os


def listFiles(directory):
    return [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]


def fileIterator(filePath, chunkSize):
    with open(filePath, "rb") as file:
        while True:
            data = file.read(chunkSize)
            if not data:
                break
            yield data


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
