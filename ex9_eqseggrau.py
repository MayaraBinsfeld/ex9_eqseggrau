"""
Programa: 
Descrição: Este programa resolve a equação de segundo grau ax^2+bx+c=0.
Autor: Mayara Binsfeld
Data: 26/02/2025
Versão: 0.0.1

"""

#### Alocação de memória
a = 0
b = 0
c = 0
import math

# Entrada de dados 

a = float(input("Qual o valor da variável a?"))
b = float(input("Qual o valor da variável b?"))
c = float(input("Qual o valor da variável c?"))

# Processamento de dados

delta = b**2 - 4*a*c
if delta < 0:
    print("Não é possível calcular raízes reais, pois o delta é negativo.")
elif a == 0:
    print("O valor de 'a' não pode ser zero, pois não seria uma equação do segundo grau.")
else:
    resultado = (-b + math.sqrt(delta))/(2*a)
    resultado2 = (-b - math.sqrt(delta))/(2*a)
    
    # Saída de dados
    print(f"O resultado de x1 é {resultado} e x2 é {resultado2}")
