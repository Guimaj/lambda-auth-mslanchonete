# mssistemalanchonete : Infra EKS

Função Lambda para autenticação do serviço [mssistemalanchonete](https://github.com/kelvinlins/mssistemalanchonete.git) via token JWT.  
Este repositório também automatiza o deploy dessa lambda e a criação da role necessaria utilizando github-actions.

## Executando via github-actions
Para executar os scripts diretamente do github, é necessário criar as secrets `JWT_SECRET, AWS_REGION, AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY`, respectivamente a secret usada no JWT, o código da região AWS, o ID e chave de acesso de um usuário AWS com permissões suficientes para criar e alterar os recursos citados acima.   
A automação ( **Deploy Lambda** ) roda a partir do merge de pull-requests para a `main`. Também é possivel acionar a automação manualmente no menu action do github.