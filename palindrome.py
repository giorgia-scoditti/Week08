# Verifico se la parola è palindroma.
# Per semplicità, usiamo una lunghezza dispari.
def is_palindrome(word):
    if len(word) == 1:
        return True # Se sono arrivato qui, la parola è palindroma.
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1]) # Estraggo la sottostringa da 1 a len - 1.

parola = input(f"Parola: ")
result = is_palindrome(parola)
print(result)