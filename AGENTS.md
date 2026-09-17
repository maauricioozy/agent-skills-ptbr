# Instruções para agentes contribuidores

Este repositório distribui skills públicas e portáteis em PT-BR.

## Ao editar

- Preserve `name` e `description` no frontmatter de cada `SKILL.md`.
- Escreva descrições curtas que indiquem quando a skill deve ser carregada.
- Mantenha no `SKILL.md` somente a rota comum. Detalhes de um único ramo ficam em `references/` e recebem um link no ponto de uso.
- Prefira critérios observáveis a adjetivos genéricos.
- Preserve a decisão do usuário, o escopo e os limites de autorização.
- Use linguagem portátil. Não fixe modelos, contas, caminhos de máquina ou ferramentas não exigidas pelo método.
- Mantenha cada regra em uma única fonte de verdade.

## Antes de concluir

Execute:

```bash
python scripts/validate_skills.py
```

Revise também o exemplo da skill alterada e registre mudanças públicas de comportamento no changelog.
