## Find all Strobogrammtic numbers of size N digits. Basically a strobogrammatic number is one that appears the same after rotating 180 degrees.

def strobonumbers(expr, i, j):
    if (j < i):
        print("".join(expr))
        return

    if (j == i):
        expr[i] = '1'
        print("".join(expr))
        expr[i] = '8'
        print("".join(expr))
        expr[i] = '0'
        print("".join(expr))
        return

    if (i != 0):
        expr[i] = '0'
        expr[j] = '0'
        strobonumbers(expr, i+1, j-1)
    
    expr[i] = '1'
    expr[j] = '1'
    strobonumbers(expr, i+1, j-1)
    expr[i] = '8'
    expr[j] = '8'
    strobonumbers(expr, i+1, j-1)
    expr[i] = '6'
    expr[j] = '9'
    strobonumbers(expr, i+1, j-1)
    expr[i] = '9'
    expr[j] = '6'
    strobonumbers(expr, i+1, j-1)

    return


if __name__ == "__main__":
    for i in range(1,4):
        expr = ['0'] * i
        strobonumbers(expr, 0, i-1)