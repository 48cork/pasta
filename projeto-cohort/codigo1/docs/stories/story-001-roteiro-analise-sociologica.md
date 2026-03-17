# Story 001 — Roteiro de Análise Sociológica - Brownfield Addition

## Status

DONE

---

## Executor Assignment

```yaml
executor: "@dev"
quality_gate: "@architect"
quality_gate_tools: ["html-validator", "browser-check"]
```

---

## User Story

**As a** estudante de sociologia,
**I want** ter acesso a um roteiro estruturado de análise sociológica na pasta `codigo1`,
**so that** eu possa conduzir pesquisas e análises de forma organizada e metodológica.

---

## Story Context

**Integração com o sistema existente:**

- Integra com: Projeto `codigo1` (Cohort ResearchMate)
- Tecnologia: HTML/CSS/JavaScript básico
- Segue o padrão: arquivos com letras minúsculas e hífen (ex: `roteiro-sociologico.html`)
- Pontos de contato: pasta raiz do `codigo1`

---

## Acceptance Criteria

1. Um arquivo `roteiro-sociologico.html` deve ser criado na pasta `codigo1`
2. O roteiro deve conter as etapas clássicas de análise sociológica:
   - Definição do objeto de estudo
   - Revisão bibliográfica
   - Escolha da metodologia (qualitativa ou quantitativa)
   - Coleta de dados
   - Análise e interpretação
   - Conclusão
3. O conteúdo deve ser apresentado de forma clara e navegável em HTML
4. O arquivo segue a convenção de nomes do projeto (letras minúsculas, hífen)
5. O visual segue o padrão simples do projeto (HTML/CSS básico, sem frameworks externos)
6. Não interfere em nenhum outro arquivo existente
7. O HTML deve ser válido e bem estruturado (doctype, charset, meta viewport)
8. O conteúdo deve usar linguagem acessível — frases curtas, sem jargão desnecessário
9. Nenhuma regressão em arquivos existentes

---

## 🤖 CodeRabbit Integration

**Story Type Analysis**
- **Primary Type**: Frontend
- **Secondary Type(s)**: Content
- **Complexity**: Baixa

**Specialized Agent Assignment**
- Primary Agents: @dev
- Supporting Agents: N/A

**Quality Gate Tasks**
- [x] Pre-Commit (@dev): Verificar HTML válido antes de marcar story completa
- [x] Pre-PR (@dev): Revisar conteúdo e estrutura antes do pull request

**Self-Healing Configuration**
- Primary Agent: @dev (light mode)
- Max Iterations: 2
- Timeout: 15 minutos
- Severity Filter: CRITICAL only

---

## Tasks / Subtasks

- [x] Task 1 — Criar arquivo `roteiro-sociologico.html` (AC: 1, 4, 7)
  - [x] 1.1 Criar o arquivo na raiz de `codigo1/` com nome correto
  - [x] 1.2 Adicionar boilerplate HTML5 válido (doctype, charset utf-8, meta viewport)
  - [x] 1.3 Adicionar `<title>` e estrutura semântica (`header`, `main`, `footer`)

- [x] Task 2 — Implementar as 6 etapas do roteiro sociológico (AC: 2, 3, 8)
  - [x] 2.1 Etapa 1: Definição do objeto de estudo
  - [x] 2.2 Etapa 2: Revisão bibliográfica
  - [x] 2.3 Etapa 3: Escolha da metodologia
  - [x] 2.4 Etapa 4: Coleta de dados
  - [x] 2.5 Etapa 5: Análise e interpretação
  - [x] 2.6 Etapa 6: Conclusão

- [x] Task 3 — Aplicar estilo CSS simples (AC: 5)
  - [x] 3.1 Adicionar `<style>` inline com fontes legíveis, espaçamento adequado
  - [x] 3.2 Destacar cada etapa visualmente (número + título + descrição)

- [x] Task 4 — Verificação final (AC: 6, 9)
  - [x] 4.1 Confirmar que nenhum outro arquivo foi modificado
  - [x] 4.2 Abrir no navegador e verificar renderização correta

---

## Dev Notes

- **Arquivo alvo:** `codigo1/roteiro-sociologico.html`
- **Stack:** HTML5 puro + CSS inline no `<style>` — sem frameworks, sem JS obrigatório
- **Convenção de nomes (CLAUDE.md):** letras minúsculas, somente hífen no nome do arquivo
- **Nível do usuário:** iniciante — linguagem simples, frases curtas, explicações diretas
- **Sem dependências externas:** não usar CDN, Google Fonts, Bootstrap, etc.

### Testing

- Abrir `roteiro-sociologico.html` diretamente no navegador (file://) e verificar:
  - Todas as 6 etapas aparecem
  - Layout legível em tela desktop
  - Nenhum erro no console do navegador
- Verificar que `git status` não mostra alterações em arquivos preexistentes

---

## Technical Notes

- **Abordagem de integração:** Arquivo standalone adicionado à raiz do `codigo1`
- **Referência de padrão existente:** Convenção de nomes do CLAUDE.md (letras minúsculas, hífen)
- **Restrições:** Sem frameworks ou bibliotecas externas — HTML/CSS puro

---

## Definition of Done

- [x] Arquivo `roteiro-sociologico.html` criado em `codigo1/`
- [x] Etapas do roteiro sociológico presentes e claras
- [x] Nomenclatura segue padrão do projeto
- [x] HTML válido e funcional no navegador
- [x] Nenhum arquivo existente foi alterado

---

## Risk Assessment

- **Risco principal:** Conteúdo muito complexo para o nível iniciante
- **Mitigação:** Linguagem simples, sem jargão acadêmico desnecessário
- **Rollback:** Deletar o arquivo `roteiro-sociologico.html` (mudança isolada)

---

## Compatibility Check

- [x] Nenhuma quebra de APIs existentes
- [x] Sem alterações em banco de dados
- [x] Segue o padrão visual existente
- [x] Impacto de performance negligível

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-03-07 | 1.0 | Story criada | Morgan (PM) |
| 2026-03-07 | 1.1 | Secoes faltantes adicionadas, status Approved | Dex (Dev) |

---

## Dev Agent Record

### Agent Model Used

claude-sonnet-4-6

### Debug Log References

N/A

### Completion Notes List

- Story corrigida (Executor Assignment, Tasks/Subtasks, CodeRabbit Integration, Change Log)
- Status alterado de draft para Approved
- Implementação iniciada com autorização do usuário

### File List

- `codigo1/roteiro-sociologico.html` — criado

---

## Metadata

```yaml
story_id: STORY-001
status: DONE
prioridade: media
estimativa: 1-2 horas
criado_em: 2026-03-07
criado_por: Morgan (PM Agent)
aprovado_por: Dex (Dev) — autorizado pelo usuário
```
