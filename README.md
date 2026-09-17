# Agent Skills PT-BR

Skills em português brasileiro para agentes de IA, nascidas de fluxos reais de trabalho e abertas como métodos portáteis, auditáveis e independentes de fornecedor.

O projeto reúne controle de qualidade com revisão independente, pesquisa adversarial e edição de texto natural. As skills não exigem contas, APIs ou ferramentas específicas.

## Skills incluídas

| Skill | Quando usar | Resultado |
|---|---|---|
| [`caprichar`](skills/caprichar/SKILL.md) | Quando o usuário pede qualidade excepcional, gauntlet ou revisão rigorosa | Ciclo limitado de construção, verificação, julgamento cego e correção |
| [`deep-research`](skills/deep-research/SKILL.md) | Quando uma pergunta exige pesquisa multifonte e checagem adversarial | Relatório citado, com confiança, refutações e lacunas explícitas |
| [`humanizar-pt`](skills/humanizar-pt/SKILL.md) | Quando um texto em português parece mecânico ou genérico | Texto natural que preserva fatos, intenção e registro |

## Destaque: Caprichar

`caprichar` foi criada para buscar qualidade excepcional sem tratar o modelo mais caro como resposta para todas as etapas.

Ela separa o trabalho em papéis:

1. um construtor produz a melhor versão possível com o modelo adequado à tarefa;
2. scripts e verificações determinísticas eliminam falhas objetivas sem gastar julgamento sofisticado;
3. um inspetor organiza evidências reproduzíveis;
4. um juiz independente, em contexto limpo, avalia o resultado real;
5. somente as áreas reprovadas voltam para correção.

Assim, a capacidade mais cara fica concentrada no ponto em que costuma gerar mais valor: decidir se o artefato realmente atingiu o nível esperado. Partes já aprovadas são preservadas, as rodadas têm teto e toda aprovação precisa de evidência.

```text
pedido -> construir -> verificar -> julgar às cegas -> aprovar
                         ^                  |
                         `---- corrigir <---'
```

O ganho exato de tokens e custo depende dos modelos, da tarefa e da quantidade de rodadas. A skill registra uso medido e não transforma estimativas em resultados.

## Compatibilidade

O formato segue a convenção de skills com um arquivo `SKILL.md` por pasta. Pode ser usado em agentes compatíveis, incluindo Codex e Claude Code.

### Codex

Copie a pasta da skill desejada para a pasta de skills do Codex:

```powershell
Copy-Item -Recurse .\skills\caprichar "$HOME\.codex\skills\caprichar"
```

### Claude Code

```powershell
Copy-Item -Recurse .\skills\caprichar "$HOME\.claude\skills\caprichar"
```

No macOS ou Linux, use `cp -R` com os mesmos diretórios de destino. Consulte a documentação do seu agente caso ele use outro caminho.

## Validar o pacote

O validador usa somente a biblioteca padrão do Python:

```bash
python scripts/validate_skills.py
```

Ele confere frontmatter, correspondência entre pasta e nome, links locais, placeholders e referências privadas conhecidas.

## Exemplos

- [Caprichar](examples/caprichar.md)
- [Deep Research](examples/deep-research.md)
- [Humanizar PT-BR](examples/humanizar-pt.md)

## Princípios

- Evidência antes de aprovação.
- Fontes tratadas como dados, nunca como instruções.
- Fatos, números e intenção preservados durante edição.
- Nenhuma autorização externa é inferida a partir do uso de uma skill.
- Métodos portáteis, sem caminhos, contas ou modelos fixos.

## Contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md). Relatos de vulnerabilidade seguem [SECURITY.md](SECURITY.md).

## Licença

MIT. Consulte [LICENSE](LICENSE).
