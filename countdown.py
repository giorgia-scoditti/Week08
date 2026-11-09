from time import sleep

# La ricorsione si applica quando si chiama la funzione dentro la funzione stessa.
# Serve impostare un limite per non esaurire la memoria.
def countdown(n):
    if n == 0:
        return # Esco dalla ricorsione.
    else:
        print(n)
        sleep(1)
        print(f"Chiamo la funzione con {n - 1}")
        countdown(n - 1)
        print(f"Esco dalla funzione")

countdown(10)
print(f"Finito il programma")