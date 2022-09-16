from wsgiref.validate import InputWrapper


base = input("Digite a área:")
altura = input("Digite a altura:")

area = float(base)*float(altura)
perimetro = (float(base)*2) + (float(altura)*2)

print("Valor da area é:",area)
print("Valor do perimetro",perimetro)