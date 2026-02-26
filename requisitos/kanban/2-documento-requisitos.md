# Documento de Requisitos — Tela de Login

## 1. Síntese da Funcionalidade
A funcionalidade de login permite que usuários autenticados acessem o sistema web com segurança.

---

## História do Usuário
Como usuário do sistema,  
Quero inserir meu e-mail e senha  
Para acessar minha conta com segurança.

---

## Regras de Negócio

RN01: O usuário deve possuir cadastro prévio.  
RN02: O e-mail deve estar em formato válido.  
RN03: A senha deve conter no mínimo 8 caracteres.  
RN04: Após 5 tentativas inválidas, a conta será bloqueada por 15 minutos.  
RN05: As senhas devem ser armazenadas com criptografia.

---

## Requisitos Funcionais

RF01: O sistema deve exibir campos de e-mail e senha.  
RF02: O sistema deve permitir inserção de credenciais.  
RF03: O sistema deve validar os dados informados.  
RF04: O sistema deve permitir acesso com credenciais válidas.  
RF05: O sistema deve exibir mensagem de erro para credenciais inválidas.  
RF06: O sistema deve permitir recuperação de senha.

---

## Requisitos Não Funcionais

RNF01: O login deve responder em até 2 segundos.  
RNF02: O sistema deve garantir segurança dos dados.  
RNF03: A interface deve ser responsiva.  
RNF04: O sistema deve ter disponibilidade mínima de 99,5%.

---

## Critérios de Aceitação

CA01: Dado que o usuário informe dados válidos, quando clicar em entrar, então o acesso deve ser permitido.  
CA02: Dado que o usuário informe dados inválidos, então deve aparecer mensagem de erro.  
CA03: Dado 5 tentativas incorretas, então a conta deve ser bloqueada temporariamente.  
CA04: Dado que o usuário clique em "Esqueci minha senha", então deve ser redirecionado para recuperação.