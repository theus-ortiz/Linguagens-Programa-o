def calculo_idade(dias):
    anos = dias // 365
    dias_resto = dias % 365
    meses = dias_resto // 30
    dias_resultado = dias_resto % 30
    return anos, meses, dias_resultado

nome_usuario = str(input("Digete seu nome: "))
idade_usuario = int(input("Digite a sua idade em dias: "))

anos, meses, dias = calculo_idade(idade_usuario)

print(f"{nome_usuario}, a sua idade fracionada é de {anos} anos, {meses} meses e {dias} dias.")
