# 🔢 Calculadora de Bases Numéricas  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![Status](https://img.shields.io/badge/Status-Ativo-success?style=flat)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindas-orange)  

Um projeto em **Python**, bem simples, que permite converter números entre diferentes bases (binário, octal, decimal e hexadecimal) e realizar operações matemáticas entre eles.  

---

# 📌 Funcionalidades  

✅ Conversão de qualquer número entre as bases **2, 8, 10 e 16**  
✅ Operações matemáticas básicas (**soma, subtração, multiplicação e divisão**) entre números em bases diferentes  
✅ Tratamento de erros (número inválido, divisão por zero, etc.)  
✅ Código modularizado em múltiplos arquivos para melhor organização  

---

# 📂 Estrutura do Projeto  

```

📦 calculadora-bases
┣ 📜 main.py          # Arquivo principal (menu interativo)
┣ 📜 conversao.py     # Funções de validação e conversão de números
┣ 📜 operacoes.py     # Funções de operações matemáticas
┗ 📜 README.md        # Documentação do projeto

````

---

## ▶️ Como Executar  

1. Clone o repositório ou baixe os arquivos.  
2. Certifique-se de que tem o **Python 3.x** instalado.  
3. No terminal, execute:  

```bash
python main.py
````

---

## 🖥️ Exemplo de Uso

### 🔹 Conversão de números

```
===== CALCULADORA DE BASES =====
1 - Converter número
2 - Operações entre números
0 - Sair
Escolha uma opção: 1
Digite o número: 1010
Base do número (2-Binário, 8-Octal, 10-Decimal, 16-Hexadecimal): 2

Decimal: 10
Binário: 1010
Octal: 12
Hexadecimal: A
```

### 🔹 Operações entre números

```
===== CALCULADORA DE BASES =====
1 - Converter número
2 - Operações entre números
0 - Sair
Escolha uma opção: 2
Digite o primeiro número: A
Base do primeiro número (2/8/10/16): 16
Digite o segundo número: 1010
Base do segundo número (2/8/10/16): 2

Resultados em decimal:
Soma: 20
Subtração: 0
Multiplicação: 100
Divisão: 1.0
```

---

# 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/) 🐍

---

# ✨ Melhorias Futuras

* [ ] Suporte a mais bases numéricas (ex.: base 36)
* [ ] Interface gráfica (GUI) com Tkinter ou PyQt
* [ ] Exportar resultados em arquivo `.txt` ou `.csv`

---

# 👨‍💻 Autor

Projeto desenvolvido por **Mayan Gabriel (mayandev1)** 🚀