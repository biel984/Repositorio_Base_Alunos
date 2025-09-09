# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 09/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

peso = float(input("informe o seu peso⚖️: "))
altura = float(input("informe a sua altura📏: "))

imc = peso / (altura*altura)

if imc < 18.5:
    print("abaixo do peso😞: ")
elif imc < 24.9:
    print("peso normal🤩: ")
elif imc < 29.9:
    print("sobrepeso😳: ")
elif imc < 34.9:
    print("obesidade grau 1😥: ")
elif imc <39.9:
     print("obsidade grau 2😭: ")
else:
    print("obesidade grau 3☠️: ")

    #Gabriel De Oliveira Cardoso 09/09/2025