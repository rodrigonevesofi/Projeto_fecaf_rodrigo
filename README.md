# Projeto: Gerenciador de Tarefas

Este repositório contém um projeto acadêmico para a disciplina de Engenharia de Software.
Objetivo: construir um sistema web simples para gerenciamento de tarefas seguindo práticas ágeis e integração contínua.

## Conteúdo
- `src/` : código fonte (Flask)
- `tests/` : testes automatizados com pytest
- `.github/workflows/ci.yml` : pipeline de CI que roda os testes
- `docs/` : documentação teórica e diagramas
- `requirements.txt` : dependências

## Como rodar (local)
1. Criar ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r src/requirements.txt
```
2. Executar a aplicação:
```bash
export FLASK_APP=src.app
export FLASK_ENV=development
flask run
```
A API ficará disponível em `http://127.0.0.1:5000`.

## Endpoints (REST)
- `GET /tasks` - lista todas as tarefas
- `POST /tasks` - cria uma tarefa (JSON: { "title": "...", "description": "..." })
- `GET /tasks/<id>` - obtém tarefa por id
- `PUT /tasks/<id>` - atualiza tarefa (JSON: fields to update)
- `DELETE /tasks/<id>` - remove tarefa

## Testes
Para executar os testes:
```bash
pytest -q
```

## Mudança de escopo (simulada)
Durante o desenvolvimento decidimos adicionar a possibilidade de marcar prioridade nas tarefas (campo `priority`). A justificativa e os commits relacionados estão descritos no `docs/` e no `docs/relatorio_teorico.docx`.

---

Trabalho desenvolvido como entrega prática do curso
# Projeto_fecaf_rodrigo
