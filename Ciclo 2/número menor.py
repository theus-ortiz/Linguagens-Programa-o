numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o primeiro número: "))
numero3 = int(input("Digite o primeiro número: "))

menor = numero1

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print(f"O menor número entre os 3 inseridos é: {menor}")