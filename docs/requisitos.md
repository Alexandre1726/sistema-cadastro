# Especificação de Requisitos — Sistema de Cadastro

## Requisitos funcionais
| ID | Descrição | Critério de aceitação |
|----|-----------|-----------------------|
| RF01 | Cadastrar usuário com nome e e-mail | Usuário salvo e listado na consulta |
| RF02 | Consultar usuários cadastrados | Lista exibe todos os registros salvos |
| RF03 | Validar e-mail no cadastro | E-mail sem "@" é rejeitado com mensagem |

## Requisitos não funcionais
| ID | Descrição |
|----|-----------|
| RNF01 | Executar em Python 3.10 ou superior, sem dependências externas |
| RNF02 | Dados persistidos em arquivo dados.json |

## Histórias de usuário
- Como administrador, quero cadastrar usuários para manter um registro organizado.
- Como administrador, quero consultar os usuários para verificar quem está cadastrado.
