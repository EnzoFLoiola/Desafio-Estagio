def sequenciaFibonacci(num):
    a = 0
    b = 1
    while a <= numeroTeste:
        if a == numeroTeste:
            return f'o {num} pertence a sequencia'
        
        aux = b
        b = a + b
        a = aux
        
    return f' o {num} não pertence'

numeroTeste = int(input('Digite o numero que deseja saber se pertence a sequencia Fibonacci: '))

resultado = sequenciaFibonacci(numeroTeste)
print(resultado)
