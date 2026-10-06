# CC8550_TesteSoftware_aula6

## Exercicio 1 (b)

| Classe | Entradas |
|---|---|
| Valida: tolerancia | 0 a 15 minutos |
| Valida: tarifa base | 16 a 180 minutos |
| Valida: faixa progressiva | 181 a 720 minutos |
| Valida: diaria | acima de 720 minutos |
| Invalida: tempo negativo | menor que 0 |
| Invalida: tipo | qualquer entrada que nao seja inteira |

A faixa de 181 a 720 e uma classe de entrada quanto ao tipo de tratamento,
mas possui fronteiras internas de cobranca: cada hora adicional ou fracao
aumenta a tarifa em R$ 3,00. Por isso, seus valores-limite tambem devem ser
testados.

## Exercicio 2 (a)

| Menor entrada | Devolvido | Esperado | Defeito |
|---|---:|---:|---|
| 0 | ValueError | R$ 0,00 | `<= 0` no lugar de `< 0` |
| 15 | R$ 12,00 | R$ 0,00 | `< 15` no lugar de `<= 15` |
| 181 | R$ 12,00 | R$ 15,00 | arredondamento para baixo |
| 720 | R$ 60,00 | R$ 39,00 | `< 720` no lugar de `<= 720` |

Tambem ha erros de arredondamento em cada fronteira interna da faixa
progressiva, como 241 minutos: a versao devolve R$ 15,00, mas o esperado e
R$ 18,00. A correcao e usar teto para `(minutos - 180) / 60`, e ajustar as
comparacoes das fronteiras.

## Exercicio 2 (b)

A suite do Exercicio 1 detecta todos os quatro defeitos, pois inclui zero,
as fronteiras 15/16, 181 e 720/721, alem das fronteiras internas do
arredondamento.

## Exercicio 2 (c)

Nao. Os representantes 8, 100, 300 e 1000 nao exercitam nenhuma das
fronteiras defeituosas: a implementacao errada devolve, respectivamente,
R$ 0,00, R$ 12,00, R$ 18,00 e R$ 60,00, todos os valores esperados.

## Exercicio 3 (a)

Na tabela reduzida, `S` significa sim, `N` significa nao e `X` significa
don't care.

| Condicao | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| Credencial especial? | S | N | N | N | N |
| Compras >= R$ 150? | X | X | S | N | N |
| Cadastro no app? | X | X | X | S | N |
| Permanencia <= 240? | X | N | S | S | S |
| Isento? | S | N | S | S | N |

Em R1, a credencial decide sozinha. Em R2, a permanencia acima de 240
decide que nao ha isencao. Em R3, compras suficientes decidem; em R4,
cadastro decide depois de compras insuficientes; R5 e o caso sem nenhum
criterio de isencao.

## Exercicio 4 (a)

A implementacao errada devolve `cadastro_app` quando a permanencia excede
240 minutos e o cliente nao tem credencial. Portanto, erra as regras
completas em que `pcd=N`, `minutos>240` e `cadastro_app=S` (com compras
abaixo ou acima de R$ 150,00). Sao duas regras da tabela completa.

## Exercicio 4 (b)

O teste do colega usava `cadastro_app=N` em R2, embora essa condicao fosse
`X`. Assim, nao verificava se o tempo continuava decisivo quando o cadastro
era verdadeiro. O caso corrigido e:

```python
(False, 200.00, True, 300, False)  # R2
```

Ele revela a implementacao errada sem alterar as cinco regras reduzidas.

## Exercicio 4 (c)

Para cada `X`, escolha concretamente valores de ambos os lados da condicao,
priorizando a combinacao que poderia fazer uma implementacao ignorar uma
condicao que ainda deveria decidir o resultado. Assim, o teste verifica que
o resultado permanece o mesmo em toda a expansao da regra reduzida.
