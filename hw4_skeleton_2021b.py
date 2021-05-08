#Skeleton file for HW4 - Spring 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include the ID number of the student submitting the solution (hw4_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#The first ID should be the ID of the student submitting the solution
#For example: SUBMISSION_IDS = ["123456000", "987654000"]
SUBMISSION_IDS = ["332390509"]

############
# QUESTION 2
############

# a
def best_mat_mult_time(L):
    #run time A*B: m_(i)*m_(i+1)*m_(i+2)
    #Stop condition:
    if len(L)==3:
        return L[0]*L[1]*L[2]

    k = min_mult(L)
    L.pop(k[0] + 1)
    return k[1] + best_mat_mult_time(L)


def min_mult(L):
    mult = {}
    for i in range(len(L)-2):
        p = L[i]*L[i+1]*L[i+2]
        mult[i] = p
    min_mult = min(mult.items(), key=lambda x: x[1])
    return min_mult

# b
def min_mult_fast(L,mu):
    min_mult = min(mu.items(), key=lambda x: x[1])
    mu.pop(min_mult[0])
    L.pop(min_mult[0])
    min_mult_fast(L, mu)
    return min_mult, L, mu

def best_mat_mult_time_fast(L):
    if len(L) ==3:
        return L[0]*L[1]*L[2]
    mu = {}
    for i in range(len(L) - 2):
        p = L[i] * L[i + 1] * L[i + 2]
        mu[i] = p
    min_mu = min(mu.items(), key=lambda x: x[1])
    mu.pop(min_mu[0])
    L.pop(min_mu[0]+1)
    print(L)
    return min_mult_fast(L, mu)[0] + min_mu[1]

print(best_mat_mult_time_fast([100,10,100,10])


# c
def best_mat_mult_order(L):
    return None



def mult_order_to_str(mult_order):
    if type(mult_order) is int:
        return str(mult_order)

    return f"({mult_order_to_str(mult_order[0])}) * ({mult_order_to_str(mult_order[1])})"



############
# QUESTION 3
############

# b
def had_local_bin(n, i_bits, j_bits):
    if n == 0:
        return 0
    n = n - 1
    current_i_bit = i_bits.pop()
    current_j_bit = j_bits.pop()
    if current_i_bit == '1' and current_j_bit == '1':
        return 0 if had_local_bin(n, i_bits, j_bits) == 1 else 1
    return had_local_bin(n, i_bits, j_bits)

#this function needs to be edited
def num_revbitlist(num, len_list):
    num_bit = bin(num)
    num_bit_len = len(num_bit)
    num_bits_list = []
    for index in range(num_bit_len - 1, 1, -1):
        num_bits_list.append(num_bit[index])
    num_bits_list.extend(['0'] * (len_list - (num_bit_len - 2)))
    return num_bits_list

def had_local(n, i, j):
    j_bits = num_revbitlist(j, n)
    i_bits = num_revbitlist(i, n)
    return had_local_bin(n, i_bits, j_bits)


# d
had_complete = lambda n : [[had_local(n, i, j) for j in range(2 ** n)] for i in range(2 ** n)]

############
# QUESTION 4
############

# a
def grid_escape1(B):
    pass  # replace this with your code

# b
def grid_escape2(B):
    pass  # replace this with your code



############
# QUESTION 5
############

# a
def partition(S):
    m = sum(S)
    if m%2 == 1:
        return None
    m = m//2
    return subset_sum_search(S, m)

def subset_sum_search(S, m):
    if (subset_sum(S,m)== False):
        return None
    return subset_finder(S,m,0,[])

def subset_sum(S, m, i=0):
    if m==0:
        return True
    if i==len(S):
        return False
    with_first = subset_sum(S, m-S[i], i+1)
    without_first = subset_sum(S, m, i+1)
    return with_first or without_first

def subset_finder(S,m,i,R):
    if m==0:
        return R
    if i==len(S):
        return None
    with_first = subset_finder(S, m - S[i], i + 1, R + [S[i]])
    without_first = subset_finder(S, m, i + 1, R)
    if (with_first == None):
        return without_first
    else:
        return with_first


# b
def n_to_k(n, k):
    memo = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        memo[i][0] = 0
    for j in range(k+1):
        memo[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (j == 1 or i == j):
                memo[i][j] = 1
            else:
                # S(n, k) = k*S(n-1, k) + S(n-1, k-1) Bell numbers
                memo[i][j] = (j * memo[i - 1][j] +
                            memo[i - 1][j - 1])

    return memo[n][k]





############
# QUESTION 6
############

def distance(s1, s2):
    return distex(s1, s2, 0, 0)


def distex(s1, s2, index_s1, index_s2):
    if len(s1) == index_s1:
        return len(s2) - index_s2
    if len(s2) == index_s2:
        return len(s1) - index_s1
    if s1[index_s1] == s2[index_s2]:
        return distex(s1, s2, index_s1 + 1, index_s2 + 1)
    return 1 + min(distex(s1, s2, index_s1 + 1, index_s2 + 1),
                   distex(s1, s2, index_s1 + 1, index_s2),
                   distex(s1, s2, index_s1, index_s2 + 1))


def distance_fast(s1, s2):
    matrix = []
    lines(len(s1) + 1, len(s2) + 1, matrix)
    return distance_mem(s1, s2, 0, 0, matrix)

def slots(num, lst):
    if num == 0:
        return 
    lst.append(None)
    num = num - 1
    slots(num, lst)


def lines(num_lines, num_columns, matrix):
    if num_lines == 0:
        return
    new = []
    slots(num_columns, new)
    matrix.append(new)
    num_lines = num_lines - 1
    lines(num_lines, num_columns, matrix)


def distance_mem(s1, s2, index_s1, index_s2, matrix):
    if len(s1) == index_s1:
        return len(s2) - index_s2
    if len(s2) == index_s2:
        return len(s1) - index_s1

    if s1[index_s1] == s2[index_s2]:
        if not matrix[index_s1 + 1][index_s2 + 1]:
            matrix[index_s1 + 1][index_s2 + 1] = distance_mem(s1, s2, index_s1 + 1, index_s2 + 1, matrix)
        return matrix[index_s1 + 1][index_s2 + 1]

    if not matrix[index_s1 + 1][index_s2 + 1]:
        matrix[index_s1 + 1][index_s2 + 1] = distance_mem(s1, s2, index_s1 + 1, index_s2 + 1, matrix)
    if not matrix[index_s1 + 1][index_s2]:
        matrix[index_s1 + 1][index_s2] = distance_mem(s1, s2, index_s1 + 1, index_s2, matrix)
    if not matrix[index_s1][index_s2 + 1]:
        matrix[index_s1][index_s2 + 1] = distance_mem(s1, s2, index_s1, index_s2 + 1, matrix)

    return 1 + min(matrix[index_s1 + 1][index_s2 + 1],
                   matrix[index_s1 + 1][index_s2],
                   matrix[index_s1][index_s2 + 1])

########
# Tester
########

def test():

    # Q2
    L1 = [100,10,100, 10]
    # a
    if best_mat_mult_time(L1) != 20000:
        print("Error in best_mat_mult_time")
    # b
    if best_mat_mult_time_fast(L1) != 20000:
        print("Error in best_mat_mult_time_fast")
    # c
    if mult_order_to_str(best_mat_mult_order(L1)) != "(0) * ((1) * (2))":
        print("Error in best_mat_mult_order")    


    # Q3
    # b
    if(had_local(2,2,2) != 1):
        print("Error in had_local")
    # d
    if had_complete(1) != [[0,0],[0,1]]:
        print("Error in had_complete")

      
    # Q4
    B1 = [[1,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,1,2]]
    B2 = [[2,3,1,2], [2,2,2,2], [2,2,3,2], [2,2,2,2]]
    B3 = [[2,1,2,1], [1,2,1,1], [2,2,2,2], [4,4,4,4]]

    # a
    if grid_escape1(B1) is False:
        print("Error in grid_escape1 - B1")
    if grid_escape1(B2) is True:
        print("Error in grid_escape1 - B2")
    if grid_escape1(B3) is True:
        print("Error in grid_escape1 - B3")

    # b
    if grid_escape2(B1) is False:
        print("Error in grid_escape2 - B1")
    if grid_escape2(B2) is False:
        print("Error in grid_escape2 - B2")
    if grid_escape2(B3) is True:
        print("Error in grid_escape2 - B3")
    

    #Q5
    # a
    if partition([3,1,1,2,2,1]) is False:
        print("Error in partition - 1")
    if partition([1,1,1]) is True:
        print("Error in partition - 2")

    # b
    if n_to_k(4,2) != 7:
        print("Error in n_to_k")


    #Q6
    if distance('computer', 'commuter') != 1 or \
            distance('sport', 'sort') != 1 or \
            distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
        print("Error in distance")

    if distance_fast('computer', 'commuter') != 1 or \
            distance_fast('sport', 'sort') != 1 or \
            distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
        print("Error in distance_fast")



