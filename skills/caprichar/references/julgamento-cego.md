# Julgamento cego

Leia este arquivo ao preparar um juiz independente.

## Contexto entregue ao juiz

Forneça somente:

- objetivo e público do entregável;
- referência a superar;
- critérios e receita de verificação;
- artefato ou caminho do resultado;
- dossiê congelado da rodada;
- falhas anteriores que precisam ser rechecadas, quando houver.

Não forneça autoria, esforço gasto, justificativas da construção ou preferência por uma versão.

## Funil de decisão

1. Verifique as falhas automáticas. Qualquer uma reprova a rodada.
2. Compare o resultado com a meta e a referência.
3. Registre a reação inicial como `uau`, `já` ou `meh`. Somente `uau` pode aprovar.
4. Liste no máximo três falhas, com a maior primeiro.
5. Para aprovar, confirme que a receita completa foi executada na versão julgada.

## Formato do veredito

```text
VEREDITO: APROVADO ou REPROVADO
REAÇÃO: uau, já ou meh
COMPARAÇÃO: superior, equivalente ou inferior à referência
EVIDÊNCIA DECISIVA: caminho ou descrição curta
FALHAS:
1. Maior falha
2. Segunda falha
3. Terceira falha
LIMITAÇÕES: o que não pôde ser conferido
```

Uma observação de polimento junto de uma aprovação não reabre automaticamente o ciclo. Registre-a separadamente para decisão posterior do usuário.
