def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10):  # testando
    print(n, "->", fib(n))
 
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def snake_case():                           # Snake case - separa as palavras por _ sendo todas a palavras minúsculas
    print()
def camelCase():                            # Camel Case - Separa as palavras por Letras maiúscula menos a primeira
    print()
def PascalCase():                           # PascalCase - Separa as palavras por Letras maiúscula
    print()



