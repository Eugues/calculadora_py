
'''
Agora, você fará a primeira parte do seu primeiro projeto! Como disse o professor Rodrigo,
não há uma forma fixa: o importante é que seu código siga uma sequência lógica e tenha, ao menos,
os critérios abaixo, ok?

Passo a passo

1. Utilize o comando "input" para receber ao menos 2 números de entrada do usuário;
2. Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);
3. Implemente ao menos 4 operações matemáticas em seu código;
4. Adicione um laço de repetição ou uma condicional. Por exemplo: você pode permitir que o usuário
escolha qual operação realizar ou criar um loop que permita ao usuário realizar várias operações
consecutivas;
5. Utilize o comando "print" para exibir o resultado da operação matemática.

'''

def obter_numero(mensagem):
    """
    Recebe um número do usuário e o converte para float.
    Se a entrada não for um número válido, solicita novamente.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Você deve digitar um número válido.")


def exibir_menu():
    """
    Exibe o menu de operações disponíveis.
    """
    print("\nEscolha a operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Comparar números (>)")
    print("6. Módulo (%)")
    print("7. Sair")


def realizar_operacao(escolha, num1, num2):
    """
    Realiza a operação matemática com base na escolha do usuário.
    """
    operacoes = {
        '1': lambda: num1 + num2,
        '2': lambda: num1 - num2,
        '3': lambda: num1 * num2,
        '4': lambda: num1 / num2 if num2 != 0 else "Erro: Divisão por zero não é permitida.",
        '5': lambda: (
            f"{num1} é maior que {num2}" if num1 > num2
            else f"{num2} é maior que {num1}" if num1 < num2
            else f"{num1} e {num2} são iguais."
        ),
        '6': lambda: num1 % num2 if num2 != 0 else "Erro: Módulo por zero não é permitido."
    }

    if escolha in operacoes:
        resultado = operacoes[escolha]()
        if isinstance(resultado, (int, float)):
            print(f"Resultado: {resultado}")
        else:
            print(resultado)
    else:
        print("Opção inválida. Tente novamente.")


def calculadora():
    """
    Função principal que implementa uma calculadora simples.
    Permite ao usuário escolher uma operação, inserir dois números e realizar a operação.
    As operações disponíveis incluem adição, subtração, multiplicação, divisão,
    comparação de números e cálculo do módulo.
    """
    print("\n\nCalculadora!")

    while True:
        exibir_menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '7':
            print("Saindo da calculadora...")
            break

        num1 = obter_numero("\nDigite o primeiro número: ")
        num2 = obter_numero("\nDigite o segundo número: ")
        realizar_operacao(escolha, num1, num2)


# Chama a função calculadora para iniciar o programa
calculadora()
