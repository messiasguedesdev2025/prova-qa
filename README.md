# Desafio QA - Sistema de Descontos

## 📋 Sobre o projeto

Este projeto foi desenvolvido como parte de um desafio prático de QA da Tech UniDiasUp.

O objetivo foi validar uma função responsável por calcular descontos em um sistema de E-commerce, utilizando testes unitários automatizados com **Python** e **Pytest**.

Durante a atividade, foram analisados os critérios de aceite da User Story, criados cenários de teste, identificados bugs no código original e realizada a correção da implementação.

## 🎯 Regras de negócio

A função `calcular_desconto(valor_compra, tipo_cliente)` deve seguir as seguintes regras:

- Compras abaixo de R$ 100,00 não recebem desconto base.
- Compras entre R$ 100,00 e R$ 499,99 recebem 10% de desconto.
- Compras iguais ou superiores a R$ 500,00 recebem 20% de desconto.
- Clientes VIP recebem mais 5% de desconto.
- O reconhecimento do cliente VIP não deve depender de letras maiúsculas ou minúsculas.
- O desconto máximo permitido é de R$ 200,00.

## 🧪 Testes realizados

Foram criados **18 testes automatizados**, contemplando:

- Compras abaixo de R$ 100,00;
- Compra exatamente de R$ 100,00;
- Compras entre R$ 100,00 e R$ 499,99;
- Compra exatamente de R$ 500,00;
- Compras acima de R$ 500,00;
- Clientes COMUM;
- Clientes VIP;
- Diferentes formas de escrita de "VIP";
- Aplicação do teto máximo de R$ 200,00;
- Valores de compra em diferentes faixas.

Também foram considerados dados inesperados, como valores negativos e tipos de cliente não previstos na regra. Esses casos não foram utilizados como critérios obrigatórios porque seu comportamento não estava definido na User Story.

## 🐛 Bugs encontrados

Durante a execução dos testes com o código original, foram encontrados dois principais bugs:

### 1. Erro no limite de R$ 100,00

O código utilizava `> 100`, fazendo com que uma compra exatamente de R$ 100,00 não recebesse o desconto de 10%.

A correção foi utilizar `>= 100`.

### 2. Identificação do cliente VIP

O código reconhecia apenas `"VIP"` em letras maiúsculas. Com isso, valores como `"vip"` e `"Vip"` não recebiam os 5% adicionais.

A correção foi utilizar `tipo_cliente.upper() == "VIP"`.

## 🔧 Tecnologias utilizadas

- Python 3.14
- Pytest 9.1.1
- Git
- GitHub

## ▶️ Como executar o projeto

Instale o Pytest:

```bash
python -m pip install pytest
