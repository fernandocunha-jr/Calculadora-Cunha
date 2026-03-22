# Montando uma Calculadora em Python que realiza sua ação em um Terminal (CLI)

#1º Passo: Definir como funcionara as operções; Em caso de erro voltar com "return" Erro.
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def mutiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

#2º Passo: Montar as primeiras mensagens que irão aparecer para o usuário.
print("------Calculadora CUNHA--------")
print("Escolha sua operação:")
print("1. Soma")
print("2. Subtração")
print("3. Mutiplicação")
print("4. Divisão")

#3º Passo: Montar a estrtura de escolha da operação em primeiro, seguido pela escolha de dois números;
#Input = inserção de dados / Float = Para o dado inserido ser um número real.
escolha = input("Escolha a sua operação (1/2/3/4):")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))

#4º Passo: A estrutura final da calculadora, onde conforme as respostas acima, gera-se o resultado. Testa das condições;
#If, Elif e Else, Se, Senão e Se não exister se e senão volta "Operação Inválida".
if escolha == "1":
    print("Resultado:", soma(num1, num2))
elif escolha == "2":
    print("Resultado:", subtracao(num1, num2))
elif escolha == "3":
    print("Resultado:", mutiplicacao(num1, num2))
elif escolha == "4":
    print("Resultado:", divisao(num1, num2))
else:
    print("Operação inválida")
