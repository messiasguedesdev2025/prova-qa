## Cenários de teste

Os testes automatizados em `test_calculadora.py` cobrem:

| Cenário | Resultado esperado |
| --- | ---: |
| Cliente comum abaixo de R$ 100 | Sem desconto |
| Cliente comum em R$ 100 | 10% de desconto |
| Cliente comum dentro da faixa de R$ 100 a R$ 499 | 10% de desconto |
| Cliente comum em R$ 500 ou acima | 20% de desconto |
| Cliente VIP abaixo de R$ 100 | 5% de desconto |
| Cliente VIP na faixa de R$ 100 a R$ 499 | 15% de desconto |
| VIP em maiúsculo, minúsculo e capitalização mista | Mesmo desconto VIP |
| Desconto calculado acima do teto | Limitado a R$ 200 |

## Evidência da execução

Comando: `python -m pytest -q`

Antes da correção: **3 falhas e 9 aprovações**. As falhas identificaram a exclusão indevida de compras de exatamente R$ 100 e a comparação de VIP sensível a maiúsculas/minúsculas.

Depois da correção: executar o mesmo comando para validar todos os cenários.
