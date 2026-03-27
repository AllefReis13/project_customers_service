# Customer Services & Schedule Project 🚀

Sistema de gestão de clientes e agendamentos desenvolvido em **Python CLI** (Interface de Linha de Comando), focado em organização modular e integridade de dados.

## 📌 Funcionalidades Atuais
- **Gestão de Clientes:** Cadastro estruturado com nome, telefone e suporte a múltiplos endereços.
- **Sanitização de Dados:** Normalização automática de entradas (limpeza de espaços e padronização) para garantir buscas precisas.
- **Interface Limpa:** Sistema de navegação com limpeza de ecrã automática e menus intuitivos.
- **Resiliência:** Tratamento de erros (`try/except`) para evitar que o programa feche por entradas inválidas.

## 📂 Estrutura do Projeto
A aplicação está dividida em módulos para facilitar a manutenção e expansão:
- `main.py`: O "cérebro" do sistema. Gere o menu principal e o fluxo de navegação.
- `customers.py`: Contém toda a lógica de negócio de clientes (adicionar, listar e procurar).
- `utils.py`: Funções de suporte (limpeza de ecrã multiplataforma e formatadores de texto).
- `schedule.py`: (Em desenvolvimento) Gestão de horários vinculados aos clientes.

## 🛠️ Tecnologias e Conceitos Aplicados
- **Lógica de Programação:** Uso de Dicionários Aninhados e Listas para estruturas de dados complexas.
- **Modularização:** Separação de responsabilidades em múltiplos ficheiros.
- **UX/UI no Terminal:** Feedback visual ao utilizador e formatação de texto (`capitalize`, `strip`, `lower`).

## 🚀 Como Executar
1. Certifica-te de que tens o Python 3 instalado.
2. Executa o ficheiro principal:
   ```bash
   python main.py
