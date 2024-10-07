
# Calculadora em Python

## Descrição

Este projeto consiste em uma calculadora simples implementada em Python, que realiza seis operações matemáticas: adição, subtração, multiplicação, divisão, comparação de números e cálculo do módulo. A calculadora permite ao usuário realizar várias operações consecutivas até que ele decida sair.

## Funcionalidades

- Recebe dois números do usuário.
- Converte as entradas para números de ponto flutuante.
- Implementa as seguintes operações:
  - Adição
  - Subtração
  - Multiplicação
  - Divisão
  - Comparação de números
  - Módulo
- Permite que o usuário escolha a operação desejada através de um menu interativo.
- Inclui uma verificação para operações inválidas.
- Utiliza um loop para permitir a execução de múltiplas operações consecutivas.

## Código da Calculadora

```python
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
```

## Execução da Calculadora

1. **Preparação do Ambiente**: Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

2. **Salvar o Código**: Salve o código da calculadora acima em um arquivo chamado `calculadora.py` ou baixe os arquivos.

3. **Executar o Script**:
   - Abra um terminal.
   - Navegue até o diretório onde o arquivo `calculadora.py` está localizado.
   - Execute o seguinte comando:
     ```bash
     python3 calculadora.py
     ```

4. **Utilização da Calculadora**:
   - Ao executar o script, um menu será exibido com as operações disponíveis.
   - Digite o número correspondente à operação desejada.
   - Insira os dois números solicitados.
   - O resultado da operação será exibido.
   - Você pode realizar várias operações consecutivas. Para isso, repita os passos de seleção da operação e entrada dos números.

5. **Finalizando a Calculadora**:
   - Para sair da calculadora, digite `7` quando solicitado a escolher a operação.

## Shell Script para Automatização

Um shell script também foi criado para automatizar a execução da calculadora. Aqui está o código do shell script:

```bash
#!/bin/bash
# Cabeçalho
echo "=== Calculadora Automática ==="
echo "Este script executa a calculadora em Python do exercício anterior."

# Comando cria diretório de logs, se não existir
mkdir -p ~/modulo1/linux/calculadora_logs

# Comando registra data e hora no log
echo "Script executando em: $(date)" >> ~/modulo1/linux/calculadora_logs/log.txt

# Comando executa a calculadora
python3 calculadora.py

# Comando verifica se a execução foi bem-sucedida e registra no log
if [ $? -eq 0 ]; then
    echo "Calculadora executada com sucesso!" >> ~/modulo1/linux/calculadora_logs/log.txt
else
    echo "Erro na execução da calculadora." >> ~/modulo1/linux/calculadora_logs/log.txt
fi

echo "Encerrando Calculadora!"
```

## Execução do Shell Script

1. **Salvar o Script**: Salve o código do shell script acima em um arquivo chamado `calculadora.sh` ou baixe o aquivo no diretório do seu dispositivo de onde será executado. No meu caso estou usando o WSL do Windows e a versão do terminal Ubuntu é a 24.04.1 LTS.
e os arquivos foram criados em `/home/eugues/modulo1/linux`.

2. **Dar Permissão de Execução**:
   - No terminal, navegue até o diretório onde o script está salvo e execute:
     ```bash
     chmod 744 calculadora.sh
     ```

3. **Executar o Shell Script**:
   - Para rodar o script, utilize o seguinte comando:
     ```bash
     ./calculadora.sh
     ```

Esse script cria um diretório para logs, registra a data e hora da execução, executa a calculadora e verifica se a execução foi bem-sucedida.

## Resumo

Com esta documentação, você agora tem todas as informações necessárias para executar e utilizar a calculadora desenvolvida em Python, assim como para automatizar sua execução usando um shell script.
