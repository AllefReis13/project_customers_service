# Customer Services & Schedule Project 🚀

Sistema de gestão de clientes e agendamentos desenvolvido em **Python CLI** (Interface de Linha de Comando), focado em organização modular, integridade de dados e escalabilidade.

## 📌 Funcionalidades Atuais (v1.2.0)
- **Identificação Única (ID):** IDs incrementais automáticos para garantir a integridade e evitar conflitos entre registos.
- **Gestão Avançada de Clientes:** Módulo de **Update** refatorado para busca precisa por ID, permitindo edições seguras de nomes, telefones e endereços.
- **Exclusão Segura (Delete):** Implementação de remoção lógica onde o cliente é movido para uma lista de histórico (`excluded_customer`), permitindo futuras recuperações sem perda de dados.
- **Agendamento Inteligente (Schedule):** Criação de serviços vinculados diretamente ao ID do cliente, com suporte a descrição, data, hora e status.
- **Cálculo de Orçamento:** Sistema dinâmico na criação de agendamentos que permite escolher entre **Valor Fixo** ou **Cálculo por Hora** (Valor/h x Quantidade).
- **Sanitização de Dados:** Normalização automática de entradas (`strip`, `lower`, `capitalize`) para garantir buscas e exibições padronizadas.
- **Interface e Resiliência:** Navegação modular com limpeza de ecrã e tratamento robusto de erros (`try/except`) para entradas inválidas.

## 📂 Estrutura do Projeto
A aplicação está dividida em módulos para facilitar a manutenção:
- `main.py`: O "cérebro" do sistema. Gere o menu principal e o fluxo de navegação.
- `customers.py`: Lógica de negócio de clientes (Cadastro, Listagem, Atualização e Exclusão com Histórico).
- `schedule.py`: Gestão de agendamentos e orçamentos vinculados aos clientes ativos.
- `utils.py`: Funções de suporte (limpeza de ecrã e normalização de texto).

## 🛠️ Tecnologias e Conceitos Aplicados
- **Dicionários Aninhados e Listas:** Estruturas complexas para armazenar múltiplos endereços e históricos de serviços por cliente.
- **Modularização:** Separação total de responsabilidades em múltiplos ficheiros (.py).
- **Lógica de Fluxo:** Busca em coleções e manipulação de estados de agendamento em tempo real.
- **Versionamento:** Uso de Git/GitHub com boas práticas de mensagens de commit e `.gitignore`.

## 🚀 Como Executar
1. Certifica-te de que tens o Python 3 instalado.
2. Executa o ficheiro principal:
   ```bash
   python main.py

