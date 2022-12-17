import numpy as np


def diag(cols, rows, args):

    rows = int(rows)
    cols = int(cols)
    matrix = []

    args = [int(x) for x in args.split('_')]

    print(type(args))

    for i in range(int(rows)):
        matrix.append(args[i * cols:(i + 1) * cols])
        print(matrix[i])

    print(matrix)

    return np.diag(np.diag(np.matrix(matrix)))