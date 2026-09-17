---
name: caprichar
description: "Executa um ciclo limitado de construir, verificar, julgar às cegas e corrigir quando o usuário pede qualidade excepcional, gauntlet ou revisão rigorosa; não use em tarefas triviais ou já aprovadas."
metadata:
  version: "0.1.0"
  language: "pt-BR"
---

# Caprichar

Use um gauntlet de qualidade quando apenas funcionar não basta. Separe construção, inspeção objetiva e julgamento. Uma aprovação precisa de evidência sobre o resultado real.

## Alocação eficiente

Distribua capacidade por papel em vez de usar o modelo mais caro durante todo o ciclo:

- **Construção e correção:** use o modelo menos caro que ainda seja capaz de executar bem a tarefa.
- **Verificação determinística:** prefira scripts, testes e medições reproduzíveis.
- **Inspeção objetiva:** use automação ou um modelo rápido quando os critérios estiverem claros.
- **Julgamento:** reserve o modelo mais capaz disponível para uma avaliação independente em contexto limpo, quando essa diferença de capacidade puder mudar o veredito.

Não troque modelos silenciosamente. Registre o papel, o modelo usado e o consumo realmente medido. Economia é consequência do roteamento e da correção focada, não uma porcentagem presumida.

## Preparação

1. Defina a meta, a referência a superar e os critérios observáveis.
2. Classifique a tarefa como pequena, média ou grande. Use no máximo 2, 4 ou 8 rodadas, respectivamente.
3. Divida entregáveis grandes em partes independentes por característica. Mantenha juntos os elementos cuja qualidade depende da interação entre eles.
4. Registre limites de tempo, tokens, dinheiro e efeitos externos. Usar esta skill não autoriza publicação, compra, deploy, envio ou alteração de produção.

## Ciclo

### 1. Construir

Produza a melhor versão possível usando as ferramentas e referências adequadas ao domínio. O construtor faz um auto-check objetivo antes de entregar, mas não aprova o próprio trabalho.

### 2. Preparar a verificação

Defina uma receita reproduzível para observar o resultado real. Transforme medições repetíveis em script quando isso reduzir erro ou retrabalho. Teste o instrumento uma vez antes de confiar nele.

Leia [references/evidencias.md](references/evidencias.md) quando o entregável precisar de renderização, interação, logs, frames ou medições.

### 3. Inspecionar

Aplique os critérios objetivos ao mesmo dossiê de evidências que será entregue ao juiz. Uma falha automática devolve o trabalho para correção antes do julgamento subjetivo.

### 4. Julgar às cegas

O juiz recebe o resultado, a meta, a referência, a receita e o dossiê. Ele não recebe autoria, justificativas nem histórico da construção. Use um agente ou contexto independente quando o ambiente permitir. Quando isso não for possível, declare que a revisão não foi verdadeiramente cega.

Leia [references/julgamento-cego.md](references/julgamento-cego.md) antes de montar o briefing e registrar o veredito.

### 5. Corrigir

Corrija a maior falha primeiro e preserve o que já foi aprovado. Refazer do zero exige uma razão concreta. Depois da correção, repita inspeção e julgamento somente nas áreas afetadas. A rodada que aprova executa a receita completa.

## Estados finais

Cada parte termina em um destes estados:

- **Aprovada:** superou a referência e passou pela receita completa.
- **Estagnada:** a mesma maior falha sobreviveu a duas rodadas de correção.
- **Esgotada:** atingiu o limite de rodadas ou orçamento.

O processo termina quando todas as partes têm um estado final. O relatório registra meta, referência, rodadas, evidências, limitações, gastos medidos e falhas restantes.

## Regras de integridade

- Julgue o artefato real, não apenas o código ou a intenção.
- Congele as evidências de cada rodada enquanto estiverem sendo avaliadas.
- Trate números sem método ou fonte como não medidos.
- Preserve qualquer item já aprovado pelo usuário até receber autorização explícita para alterá-lo.
- Relate limitações e estagnações sem suavizar o resultado.
