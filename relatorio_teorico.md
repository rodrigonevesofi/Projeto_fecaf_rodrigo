
Trabalho: Construindo um Projeto Ágil no GitHub
Aluno: Rodrigo Neves Vieira

1. Descrição do projeto e escopo inicial
Este projeto tem como objetivo desenvolver um sistema web simples para gerenciamento de tarefas (To-Do).
No escopo inicial estava apenas o CRUD de tarefas com campos básicos: título, descrição e estado (feito/não feito).

2. Metodologia ágil utilizada
Adotei um fluxo Kanban simples (To Do, In Progress, Done). Para este trabalho foquei em iterações curtas, 
priorizando funcionalidades essenciais primeiro (MVP) e posteriormente adicionando pequenas melhorias.

3. Importância da modelagem
A modelagem ajuda a organizar as entidades e responsabilidades. Criei um Diagrama de Casos de Uso e um Diagrama de Classes 
simples para documentar como os usuários interagem com o sistema e como as tarefas são representadas.

4. Diagramas UML (simples)
Diagrama de Casos de Uso:
- Ator: Usuário
- Casos: Criar tarefa, Listar tarefas, Editar tarefa, Remover tarefa, Marcar como concluída.

Diagrama de Classes (resumido):
- Classe Task
  - id: int
  - title: string
  - description: string
  - done: boolean
  - priority: int

5. Justificativa da mudança de escopo
Durante o desenvolvimento decidi adicionar o campo `priority` para permitir priorização de tarefas críticas, pois o cliente (startup fictícia) solicitou priorizar tarefas urgentes.

6. Testes automatizados
Implementei testes com pytest para garantir que as operações básicas do CRUD funcionem e que a API responda corretamente a casos de erro.

7. Prints e evidências (instruções)
- Kanban: criar um board no GitHub Projects com colunas To Do, In Progress e Done e ao menos 10 cards (simulados).
- Commits: Faça commits frequentes com mensagens claras (ex.: feat: adicionar endpoint POST /tasks).
- Workflow: adicionar o arquivo `.github/workflows/ci.yml` para rodar os testes automaticamente.

8. Conclusão (reflexão)
Este trabalho me ajudou a aplicar conceitos de engenharia de software e práticas ágeis. A integração contínua com GitHub Actions oferece confiança para mudanças rápidas sem quebrar funcionalidades existentes.
