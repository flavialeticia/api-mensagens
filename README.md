# api-mensagens

Objetivo
Desenvolver uma API básica para gerenciamento de mensagens utilizando as operações CRUD (Criar, Ler, Atualizar, Deletar), realizando testes no Postman e utilizando o ambiente GitHub Codespaces para execução.

Tarefa
1. Crie um repositório público no seu GitHub com o nome 'api-mensagens'.
2. Desenvolva uma API para gerenciar uma tabela de 'mensagens' com os campos 'id' (identificador único) e 'conteudo' (texto da mensagem). Você pode escolher qualquer linguagem de programação e framework web. As rotas da API devem seguir a estrutura abaixo:
• Criar uma nova mensagem (CREATE):
  - Método HTTP: POST
  - Endpoint: /mensagens
  - Corpo da Requisição:
  { "conteudo": "Texto da nova mensagem."  }

• Listar todas as mensagens (READ - ALL):
  - Método HTTP: GET
  -Endpoint: /mensagens
• Obter uma mensagem específica por ID
(READ - ONE):
  -Método HTTP: GET
  -Endpoint: /mensagens/{id}
• Atualizar o conteúdo de uma mensagem
(UPDATE):
  -Método HTTP: PUT
  -Endpoint: /mensagens/{id}
  -Corpo da Requisição:
  {
      "conteudo": "Novo texto da mensagem."
  }

• Deletar uma mensagem por ID (DELETE):
  -Método HTTP: DELETE
  -Endpoint: /mensagens/{id}

3. Execute sua API no ambiente GitHub Codespaces.
4. Crie uma coleção no Postman para testar sua API.
5. Configure uma variável de ambiente no Postman com a URL BASE da sua API em execução no Codespaces.
6. Implemente requisições na coleção do Postman para todas as rotas criadas, garantindo o funcionamento completo do CRUD.
7. Publique o código da API no repositório GitHub criado.
8. Exporte a coleção do Postman como um arquivo .json.

Entregáveis
• Link para o repositório GitHub contendo a API (api-mensagens).
• Arquivo .json da exportação da coleção do Postman.

Instruções Adicionais
Utilize a URL BASE gerada pelo GitHub Codespaces para configurar o Postman. Documente no README.md os passos necessários para executar sua API no ambiente Codespaces, se necessário.
