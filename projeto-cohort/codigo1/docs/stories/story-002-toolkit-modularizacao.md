# Story 002 — Toolkit de Modularização Sociológica

## Status

DONE

---

## User Story

**As a** estudante/pesquisador(a),
**I want** um toolkit sociológico modular com tema variável,
**so that** eu possa reutilizar o mesmo roteiro em diferentes pesquisas de campo.

---

## Acceptance Criteria

1. O arquivo `codigo1/roteiro-sociologico.html` deve adotar formato "Toolkit".
2. O tema de pesquisa deve ser variável por placeholder (`{{TEMA_DE_PESQUISA}}`).
3. Deve existir seção "Theoretical Toolbox" com: Durkheim, Weber, Marx, Bourdieu e Bauman.
4. O arquivo `codigo1/GUIA_ALUNO.md` deve trazer perguntas de entrevista por ferramenta teórica.
5. Cada ferramenta no guia deve conter 2-3 perguntas de entrevista.

---

## Tasks / Subtasks

- [x] Refatorar `roteiro-sociologico.html` para formato Toolkit
  - [x] Introduzir placeholder de tema variável
  - [x] Criar seção "Theoretical Toolbox" com 5 autores
  - [x] Incluir prompts modulares por ferramenta

- [x] Refatorar `GUIA_ALUNO.md` para formato Toolkit
  - [x] Estruturar perguntas por ferramenta teórica
  - [x] Garantir 2-3 perguntas por ferramenta
  - [x] Manter seção de ética de campo

---

## Dev Agent Record

### Completion Notes List

- HTML migrado para estrutura modular com navegação por blocos de toolkit.
- Tema transformado em variável `{{TEMA_DE_PESQUISA}}`.
- Toolbox teórica expandida para 5 autores clássicos.
- Guia pedagógico atualizado com perguntas aplicáveis em campo para cada ferramenta.

### File List

- `codigo1/roteiro-sociologico.html` — refatorado para Toolkit modular
- `codigo1/GUIA_ALUNO.md` — guia atualizado com perguntas por ferramenta
- `codigo1/docs/stories/story-002-toolkit-modularizacao.md` — criado

---

## Metadata

```yaml
story_id: STORY-002
status: DONE
prioridade: media
criado_em: 2026-03-17
```
