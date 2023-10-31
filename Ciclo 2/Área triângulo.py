a = int(input("Digite o valor do lado A: "))
b = int(input("Digite o valor do lado B: "))
c = int(input("Digite o valor do lado C: "))

if a < b + c and b < a + c and c < a + b:
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Os valores formam um triângulo de área: {area:.2f}")
else:
    print("Esse valores não formam um triângulo.")