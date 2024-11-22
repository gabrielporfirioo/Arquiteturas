# Projeto de Comparação de Arquiteturas

Este repositório contém uma aplicação de gerenciamento de contatos e compromissos implementada em três diferentes arquiteturas de software, demonstrando as diferentes abordagens de estruturação de código e organização de projetos.

## 📋 Visão Geral

O projeto implementa um sistema de gerenciamento que permite:
- Adicionar e gerenciar contatos
- Criar e gerenciar compromissos
- Estabelecer links entre contatos e compromissos

Cada implementação oferece as mesmas funcionalidades, mas utiliza uma arquitetura diferente para demonstrar as vantagens e características de cada abordagem.

## 🏗️ Arquiteturas Implementadas

### 1. Arquitetura Monolítica
- Localização: `/monolitica`
- Características:
 - Aplicação única e autocontida
 - Todos os componentes são interdependentes
 - Simplificidade na implementação e deploy

### 2. Arquitetura de Microsserviços
- Localização: `/microsservicos`
- Características:
 - Serviços independentes para contatos e compromissos
 - Comunicação entre serviços via API
 - Maior escalabilidade e manutenibilidade

### 3. Arquitetura em Camadas
- Localização: `/camadas`
- Características:
 - Separação clara entre camadas de apresentação, negócios e dados
 - Responsabilidades bem definidas para cada camada
 - Facilidade de manutenção e teste


## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Cada arquitetura pode utilizar bibliotecas específicas para sua implementação

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gabrielporfirioo/Arquiteturas.git
cd Arquiteturas
cd (arquitetura de sua escolha)
code .
```
