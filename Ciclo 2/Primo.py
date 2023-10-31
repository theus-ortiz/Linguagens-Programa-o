def primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

for num in range(1, 101):
    if primo(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")