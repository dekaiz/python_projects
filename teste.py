print("===== Faça uma divisão =====")
try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 / num2
except ValueError:
    print("Por favor digite apenas números!")
except ZeroDivisionError:
    print("Divisão por zero")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Obrigado pela visita, volte sempre!")

