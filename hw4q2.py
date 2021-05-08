

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
