def imprimir_fibonacci(n):
    a, b = 0, 1
    fibonacci = []
    while a < n:
        fibonacci.append(a)
        a, b = b, a + b
    print("Serie de Fibonacci:", fibonacci)

def suma_fibonacci(n):
    a, b = 0, 1
    suma = 0
    while a < n:
        suma += a
        a, b = b, a + b
    print("Suma de la serie de Fibonacci:", suma)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
