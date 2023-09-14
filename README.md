# API Prontuário Médico

Este é um projeto de MVP (Minimum Viable Product) de uma API Flask para gerenciar medicamentos em um prontuário médico.
Ela permite adicionar, visualizar e remover medicamentos da base de dados. 

O objetivo principal deste prontuário é fornecer uma ferramenta útil para aqueles que cuidam de pessoas idosas, enfermas ou que fazem uso de vários medicamentos.

Um dos desafios frequentes para quem cuida de alguém é responder à pergunta: "- Quais medicamentos essa pessoa está tomando?" 

Com o Prontuário, você pode manter uma lista completa de todos os medicamentos, suas respectivas posologias, o médico que os prescreveu e a especialidade desse médico.

Essa informação detalhada pode ser crucial, especialmente em situações de emergência, garantindo que os profissionais de saúde tenham acesso a dados precisos. 

Os benefícios deste prontuário são mútuos:

- O médico recebe todas as informações necessárias para tomar decisões.
- A pessoa sob cuidado recebe atendimento de qualidade e personalizado.
- O acompanhante ou cuidador ganha mais controle e confiança em fornecer assistência.

Com o Prontuário Médico, todos saem ganhando, promovendo uma melhor qualidade de cuidados de saúde e bem-estar para aqueles que precisam de assistência.

## Requisitos

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal.

Certifique-se de que você tenha  todas as libs python listadas no `requirements.txt` instaladas.

Este comando instala as bibliotecas, descritas no arquivo `requirements.txt`:

pip install -r requirements.txt

## Como Usar

Para utilizar esta API, siga os passos abaixo:

1. Inicie a aplicação Flask:

  flask run --host 0.0.0.0 --port 5000

2. Acesse a documentação Swagger para obter detalhes sobre as rotas e os parâmetros necessários.

3. Use as rotas para adicionar, visualizar ou remover medicamentos.

## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000//openapi/swagger#/](http://localhost:5000//openapi/swagger#/)

## Rotas da API

- [POST] `/medicamento`

  Adiciona um novo medicamento à base de dados.

  - **Entrada**: Um objeto JSON com os dados do medicamento.
  - **Saída**: Uma representação dos medicamentos cadastrados.

- [GET] `/medicamentos`

  Retorna uma listagem de todos os medicamentos cadastrados.

- [GET] `/medicamento`

  Retorna informações de um medicamento com base em seu nome.

- [DELETE] `/medicamento`

  Remove um medicamento com base em seu nome.

- [DELETE] `/medicamento_id`

  Remove um medicamento com base em seu Id.

## Notas de Versão

### Versão 1.0.0 (setembro/2023)

- Implementação inicial da API.
- Funcionalidade de adicionar, visualizar e remover medicamentos.

## Autor

Este projeto foi desenvolvido por Rodrigo Procópio e pode ser encontrado no [GitHub](https://github.com/RodrigoProcopio).

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENCE] (https://github.com/RodrigoProcopio/MVP_Prontuario_Medico_API/blob/main/LICENSE.md) para obter detalhes.
