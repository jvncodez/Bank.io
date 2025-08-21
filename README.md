
# 💰 JvnBank - Projeto Bootcamp Santander

Este projeto foi desenvolvido como parte do **Bootcamp Santander**, na etapa final de formação em Python.  

O **JvnBank** é um sistema bancário simples, feito em **Python**, que simula as principais operações de um banco, incluindo gerenciamento de usuários e contas, depósitos, saques e extratos.  

---

## 🚀 Funcionalidades

O sistema oferece:

- Solicitação do **nome do usuário** com mensagens de boas-vindas personalizadas.  
- Menu interativo com opções:  
1. Depositar  
2. Sacar  
3. Extrato  
4. Criar novo usuário  
5. Criar nova conta  
6. Listar contas  
0. Sair  

- **Depósitos** com registro automático no extrato.  
- **Saques** com validação de:  
  - Saldo disponível  
  - Limite diário de saque (R$ 500 por saque)  
  - Número máximo de saques por dia (3 saques)  
- Exibição do **extrato completo** de movimentações e saldo atual.  
- Criação de **usuários** com CPF, nome, data de nascimento e endereço.  
- Criação de **contas bancárias** vinculadas a usuários existentes, com agência e número de conta.  
- Listagem de todas as contas cadastradas com dados de agência, conta e titular.  
- Encerramento seguro da aplicação digitando `0`.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**  

---

## 📂 Estrutura do Projeto

```
📦 jvnbank
 ┣ 📜 main.py     # Código principal do sistema bancário
 ┗ 📜 README.md   # Documentação do projeto
```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/jvnbank.git
   ```
2. Acesse a pasta do projeto:  
   ```bash
   cd jvnbank
   ```
3. Execute o arquivo principal:  
   ```bash
   python main.py
   ```
4. Siga as instruções do menu para criar usuários, contas, fazer depósitos, saques e consultar extratos.  

---

## 📖 Aprendizados

Durante o desenvolvimento do **JvnBank**, foram reforçados conceitos importantes de Python, como:  

- Estruturas condicionais (`if/elif/else`)  
- Estruturas de repetição (`while`)  
- Manipulação de strings e números  
- Entrada e saída de dados com `input` e `print`  
- Criação de funções reutilizáveis com parâmetros posicionais e nomeados  
- Organização de código, boas práticas e clareza em mensagens ao usuário  

---

## 👨‍💻 Autor

**João Nascimento**  
Bootcamp Santander | [DIO](https://www.dio.me/)  

---

![Santander Bootcamp](https://img.shields.io/badge/Santander-Bootcamp-red?style=for-the-badge&logo=santander&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=yellow)  
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)  
