def grid_escape_param(B, i, j, m, n, c):
    if c== True:
        return True
    if c == False:
        return False

    if n < 0:
        c == True
    if m < 0:
        c == True
    if i == j >= 3:
        c == True
    step = B[i][j]

    if step > m: #is step in i direction possible?
        if step > n: #no, is step in j direction possible?
            c == False
        if j + step <4:
            if B[i][j + step] > n - step:  # yes, is step in j direction, right smart?
                if B[i][j + step] > m:  # no, is step in j direction, up smart?
                    if i==j+step==3:
                        c = True
                        grid_escape_param(B, i, j, m, n, c)
                    c == False
                j = j + step  # go j and up
                n = n - step
                grid_escape_param(B, i, j, m, n, c)
            j = j + step  # go j and right
            n = n - step
            grid_escape_param(B, i, j, m, n, c)
        else:
                c == False


    if i +step <4:
        if B[i + step][j] > m - step:  # yes, is step in i direction, up smart?
            if B[i + step][j] > n:  # no, is step in i direction, right smart?
                if step > n:  # no, is step in j direction possible?
                    c == False
                if B[i][j + step] > n - step:  # yes, is step in j direction, right smart?
                    if B[i][j + step] > m:  # no, is step in j direction, up smart?
                        c == False
                    j = j + step  # go j and up
                    n = n - step
                    grid_escape_param(B, i, j, m, n, c)
                j = j + step  # go j and right
                n = n - step
                grid_escape_param(B, i, j, m, n, c)
            i = i + step  # go i and right
            m = m - step
            grid_escape_param(B, i, j, m, n, c)
        i = i + step  # go i and up
        m = m - step
        grid_escape_param(B, i, j, m, n, c)

    else:
        if step > n:  # no, is step in j direction possible?
            c == False
        if j + step < 4:
            if B[i][j + step] > n - step:  # yes, is step in j direction, right smart?
                if B[i][j + step] > m:  # no, is step in j direction, up smart?
                    c == False
                j = j + step  # go j and up
                n = n - step
                grid_escape_param(B, i, j, m, n, c)
            j = j + step  # go j and right
            n = n - step
            grid_escape_param(B, i, j, m, n, c)
        else:
            c == False




def grid_escape1(B):
    n = len(B)-1
    m = len(B)-1
    if n < 0:
        return True
    if m < 0:
        return True
    i = 0
    j = 0
    c=2
    return grid_escape_param(B, i, j, m, n, c)

B1 = [[1,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,1,2]] #T
B2 = [[2,3,1,2], [2,2,2,2], [2,2,3,2], [2,2,2,2]] #F
B3 = [[2,1,2,1], [1,2,1,1], [2,2,2,2], [4,4,4,4]] #F

print(grid_escape_param(B1, 0,0,4,4,2))

print("1", grid_escape1(B1))
print("2", grid_escape1(B2))
print("3", grid_escape1(B3))