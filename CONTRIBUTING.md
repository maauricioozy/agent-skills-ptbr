# Como contribuir

Contribuições devem melhorar uma decisão observável do agente. Evite acrescentar regras universais para um caso isolado.

## Antes de abrir um pull request

1. Explique o comportamento que precisa mudar e apresente um exemplo reproduzível.
2. Preserve o objetivo e os limites de autorização de cada skill.
3. Mantenha instruções comuns no `SKILL.md` e detalhes condicionais em `references/`.
4. Não inclua nomes de clientes, credenciais, caminhos locais ou dados privados.
5. Execute `python scripts/validate_skills.py`.
6. Atualize o exemplo correspondente quando o comportamento público mudar.
7. Registre a mudança em `CHANGELOG.md`.

## Critério de aceitação

A alteração precisa ter escopo claro, ser portátil e melhorar uma decisão real. Reformulações sem mudança observável de comportamento podem ser recusadas.
