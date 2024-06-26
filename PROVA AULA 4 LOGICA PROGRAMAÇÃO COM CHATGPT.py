print(f"insira dois números inteiros, representando o início e o fim do intervalo.")
print(f"Nessa etapa iremos informar os numeros pares do intervalo.")
num1=int(input("digite o primeior numero inteiro: "))
num2=int(input("digite o segundo numero inteiro: "))
for num in range(num1,num2):
    if (num%2==0):
        print(f"{num}")

print(f"agora iremos informar a soma dos numeros pares do intervalo.")
soma=0
for num in range(num1,num2):
    if (num%2==0):
        soma+=num
        print(f"{soma}")