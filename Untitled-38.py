def applyF_filterG(L, f, g):
    ls = []
    for num in L:
        if g(f(num)):
            ls.append(num)
    L[:] = ls
    if len(L) == 0:
        return -1
    else:
        return max(L)