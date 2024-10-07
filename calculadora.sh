#!/bin/bash
# Cabeçalho
echo "=== Calculadora Automática EBAC ==="
echo "Este script executa a calculadora em Python do exercício anterior.."

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

