def é_palindromo(frase):

    def verifica(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return verifica(s[1:-1])
    frase = frase.replace(" ", "").lower()
    return verifica(frase)

while True:
    frase = input('Digite uma frase: ')
    if frase == "":
        break
    if é_palindromo(frase):
        print(f"A frase '{frase}' é um palíndromo.")
    else:
        print(f"A frase '{frase}' não é um palíndromo.")
