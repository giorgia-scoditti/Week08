from time import time
import scipy

c = 0
def binomial(n, m):
    if m == n or m == 0: # Cioè, (n n) = 1 o (n 0) = 1.
        return 1
    else:
        global c
        c = c + 1
        return binomial(n - 1, m - 1) + binomial(n - 1, m)

start_time = time()
b = binomial(30, 10)
print(f"Il binomiale vale: {b}")
print(f"Numero di chiamate della funzione: {c} ")
end_time = time()
print(end_time - start_time)

start_time = time()
b = scipy.special.binom(30, 10)
print(f"Il binomiale vale: {b}")
end_time = time()
print(end_time - start_time)