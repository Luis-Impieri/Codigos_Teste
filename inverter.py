def inversor(s):
    s_invertida = ''
    for caracter in s:
        s_invertida = caracter + s_invertida
    return s_invertida

s = input("Digite o seu texto que será invertido")
print(inversor(s)) 