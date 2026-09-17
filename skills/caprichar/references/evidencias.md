# Evidências reproduzíveis

Leia este arquivo quando a qualidade depender de renderização, interação, logs, frames ou medições.

## Receita mínima por tipo de entregável

| Entregável | Evidência mínima |
|---|---|
| Site ou interface | Capturas nos viewports relevantes, console sem erros, navegação e ações principais testadas |
| Aplicação interativa | Estados antes e depois das ações, fluxo principal executado e falhas registradas |
| PDF ou documento | Renderização e inspeção de todas as páginas, além da reabertura do arquivo final |
| Vídeo ou animação | Reprodução em velocidade normal, frames dos momentos críticos e conferência de áudio quando aplicável |
| Texto | Leitura integral, fatos conferidos e comparação com a voz ou referência pedida |
| Planilha ou dados | Arquivo reaberto, fórmulas ou totais recalculados e origem dos números registrada |
| Mudança remota | Leitura posterior pela interface ou API que represente o estado efetivo |

## Dossiê por rodada

Salve a evidência em uma pasta própria por rodada e não a sobrescreva durante a avaliação. Inclua:

- comando ou procedimento executado;
- ambiente relevante;
- método e limiar de cada medição;
- capturas, logs ou números resultantes;
- itens que não puderam ser conferidos.

O script mede o que é determinístico. O inspetor interpreta somente o que o código não mede com segurança.

## Falhas automáticas

Devolva para correção antes do julgamento subjetivo quando houver:

- erro oculto em console ou log;
- ação principal que não funciona;
- link ou referência quebrada;
- conteúdo cortado, sobreposto ou ilegível;
- estado final incompatível com a solicitação;
- arquivo inválido ou que não reabre;
- ausência da evidência exigida pela receita.
