def can_escape(B, i=0, j=0):
    n = len(B) - 1

    if i > n or j > n:
        return False

    if (i, j) == (n, n):
        return True

    step = B[i][j]
    if step == 0:
        return False

    return can_escape(B, i + step, j) or can_escape(B, i, j + step)

