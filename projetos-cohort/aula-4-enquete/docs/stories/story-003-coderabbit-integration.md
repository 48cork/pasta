# Story 003 - Integracao do CodeRabbit no Repositorio

## Status

Draft

---

## User Story

**As a** mantenedor(a) do repositorio,
**I want** instalar e configurar o CodeRabbit,
**so that** possamos ter revisao automatizada de PRs com feedback de qualidade de codigo.

---

## Contexto

- Repositorio alvo: `aula-4-enquete`
- Objetivo da integracao: habilitar revisao automatizada em PRs
- Escopo: instalacao, configuracao minima e validacao em fluxo real de pull request

---

## Acceptance Criteria

1. O CodeRabbit deve estar instalado e conectado ao repositorio.
2. Deve existir configuracao versionada para regras basicas de revisao (arquivo de config do CodeRabbit, quando aplicavel).
3. O fluxo de PR deve disparar revisao automatica do CodeRabbit.
4. A documentacao do projeto deve registrar como usar/manter a integracao.
5. Evidencias da validacao devem ser registradas no Dev Agent Record.

---

## Tasks / Subtasks

- [ ] Task 1 - Habilitar integracao no repositorio
  - [ ] 1.1 Conectar CodeRabbit ao repositorio correto
  - [ ] 1.2 Confirmar permissoes de acesso e escopo

- [ ] Task 2 - Configuracao inicial
  - [ ] 2.1 Criar/ajustar arquivo de configuracao do CodeRabbit
  - [ ] 2.2 Definir regras minimas (linguagem, severidade, foco)

- [ ] Task 3 - Validacao em PR
  - [ ] 3.1 Abrir PR de teste
  - [ ] 3.2 Verificar comentario/revisao automatica do CodeRabbit
  - [ ] 3.3 Registrar resultado da validacao

- [ ] Task 4 - Documentacao e fechamento
  - [ ] 4.1 Atualizar docs do projeto com instrucoes operacionais
  - [ ] 4.2 Atualizar story (checklist, file list, notas)
  - [ ] 4.3 Marcar story como DONE apos validacao completa

---

## Definition of Done

- [ ] Integracao ativa e funcional no repositorio
- [ ] Configuracao versionada
- [ ] PR de teste validado com revisao do CodeRabbit
- [ ] Documentacao atualizada

---

## Dev Agent Record

### Agent Model Used

A preencher

### Debug Log References

A preencher

### Completion Notes List

- A preencher

### File List

- `docs/stories/story-003-coderabbit-integration.md` - criado

---

## Metadata

```yaml
story_id: STORY-003
status: Draft
prioridade: media
criado_em: 2026-03-17
```

## Validação de Sprint: Teste de Agente Analista
- **Data:** 17/03/2026
- **Status:** Sucesso (Offline)
- **Resultado:** O @analyst aplicou corretamente a Metodologia Funcionalista de Durkheim em um caso real da UFCG.
- **Evidências:** O agente identificou Exterioridade, Coercitividade e Generalidade, concluindo pela presença de um Fato Social.

> **Nota do Professor Sergio:** A integração entre a estrutura técnica da Aula 4 e o conteúdo pedagógico de Sociologia I está validada e funcional.

## Evolução Epistemológica: Módulo Multiparadigmático
- **Data:** 17/03/2026
- **Update:** Implementação das lentes de Bourdieu (Praxiologia) e Durkheim (Funcionalismo).
- **Impacto Pedagógico:** O sistema agora permite aos alunos da UFCG comparar como diferentes teorias sociológicas produzem diagnósticos distintos sobre o mesmo fato social.
- **Status:** Documentação de suporte criada (`EXEMPLO_COMPARATIVO_DURKHEIM_BOURDIEU.md`).
