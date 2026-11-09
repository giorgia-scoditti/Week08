class Quicksort:
    def sort(self, sequenza):
        if len(sequenza) <= 1: # Condizone di uscita dalla ricorsione.
            return sequenza
        else:  # Eseguo la ricorsione.
            # 1. Scelgo il pivot.
            pivot = sequenza[0]

            # 2. Divido la sequenza in sottosequenze.
            sequenza_minori = []
            for i in range(1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_minori.append(sequenza[i])
            # Devo fare lo stesso per le sequenze maggiori e uguali.
            # In alternativa, molto più sinteticamente posso usare la comprehension.
            sequenza_maggiori = [n for n in sequenza if n > pivot]
            sequenza_uguali = [n for n in sequenza if n == pivot]

            # 3. Chiamo sort() sulle sottosequenze e riassemblo.
            return self.sort(sequenza_minori) + sequenza_uguali + self.sort(sequenza_maggiori)

qs = Quicksort()
sequenza = [3, 7, 11, 2, 5, 9, 4, 7]
sequenza_ordinata = qs.sort(sequenza)
print(sequenza_ordinata)