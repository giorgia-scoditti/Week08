from functools import lru_cache

class Fibonacci:
    def __init__(self):
        self.cache = {} # Serve per ottimizzare la ricerca dei valori già calcolati.
        self.cache[0] = 0
        self.cache[1] = 1

    # Di seguito, la mia funzione per il calcolo usando il dizionario.
    def calcola_elemento_usando_cache(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = self.calcola_elemento_usando_cache(n - 1) + self.calcola_elemento_usando_cache(n - 2)
            return self.cache[n]

    # Di seguito, la funzione ottimmizzata con lru_cache.
    @lru_cache(maxsize=None)
    def calcola_elemento(self, n): # Lo stato è in n.
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else :
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)

    """    
    # Di seguito, la mia funzione non ottimizzata.
    def calcola_elemento(self, n): # Lo stato è in n.
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else :
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)
    """

fib = Fibonacci()
print(f"Calcolo con la cache")
value = fib.calcola_elemento_usando_cache(50)
print(value)

fib = Fibonacci()
print(f"Calcolo senza la cache")
value = fib.calcola_elemento(50)
print(value)