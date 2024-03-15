def fibonacci(n):
    a, b = 0, 1
    sequencia = [a, b]
    while b <= n:
        a, b = b, a + b
        sequencia.append(b)
    return sequencia

def verifica_pertencimento(numero, sequencia):
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

try:
    numero_verificar = int(input("Digite um número para verificar: "))
    sequencia_fibonacci = fibonacci(numero_verificar)
    print(f"Sequência de Fibonacci até {numero_verificar}: {sequencia_fibonacci}")
    print(verifica_pertencimento(numero_verificar, sequencia_fibonacci))
except ValueError:
    print("Entrada inválida. Informe um número inteiro positivo.")