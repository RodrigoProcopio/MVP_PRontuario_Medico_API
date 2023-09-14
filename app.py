from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from model import Session, Medicamento
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Prontuário Médico", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação Swagger", description="Documentação estilo Swagger.")
medicamento_tag = Tag(name="Medicamento", description="Adição, visualização e remoção de medicamentos na base de dados.")


def home():
    """Redireciona para documentação da API no estilo Swagger.
    """
    return redirect('/openapi/swagger')

@app.post('/medicamento', tags=[medicamento_tag],
          responses={"200": MedicamentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_medicamento(form: MedicamentoSchema):
    """Adiciona um novo Medicamento à base de dados

    Retorna uma representação dos medicamentos cadastrados.
    """
    # Capitaliza a primeira letra de cada palavra no nome do medicamento
    medicine_name = form.medicine.title()

    medicamento = Medicamento(
        medicine=medicine_name,
        posology=form.posology,
        doctor=form.doctor,
        specialty=form.specialty
    )
    
    logger.debug(f"Adicionando medicamento: '{medicamento.medicine}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando medicamento
        session.add(medicamento)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado medicamento: '{medicamento.medicine}'")
        return apresenta_medicamento(medicamento), 200

    except IntegrityError as e:
        # A duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Um medicamento com o mesmo nome já existe."
        logger.warning(f"Erro ao adicionar medicamento '{medicamento.medicine}', {error_msg}")
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso ocorra um erro fora do previsto
        error_msg = "Não foi possível salvar um novo medicamento."
        logger.warning(f"Erro ao adicionar medicamento '{medicamento.medicine}', {error_msg}")
        return {"mensagem": error_msg}, 400
    
@app.get('/medicamentos', tags=[medicamento_tag],
         responses={"200": ListagemMedicamentosSchema, "404": ErrorSchema})
def get_medicamentos():
    """Faz a busca por todos os Medicamentos cadastrados.

    Retorna uma representação da listagem de medicamentos.
    """
    logger.debug(f"Coletando medicamentos ")

    session = Session()
    medicamentos = session.query(Medicamento).all()

    if not medicamentos:
        return {"medicamentos": []}, 200
    else:
        logger.debug(f"%d medicamentos econtrados" % len(medicamentos))
        print(medicamentos)
        return apresenta_medicamentos(medicamentos), 200


@app.get('/medicamento', tags=[medicamento_tag],
         responses={"200": MedicamentoViewSchema, "404": ErrorSchema})
def get_produto(query: MedicamentoBuscaSchema):
    """Faz a busca por um Medicamento a partir do nome do medicamento

    Retorna uma representação dos medicamentos cadastrados.
    """
    medicamento_medicine = query.medicine.strip().lower()  # Remove espaços e converte para minúsculas
    logger.debug(f"Coletando dados sobre medicamento #{medicamento_medicine}")

    session = Session()

    # fazendo a busca, usando ilike para busca insensível a maiúsculas/minúsculas
    medicamento = session.query(Medicamento).filter(func.lower(Medicamento.medicine).ilike(f"%{medicamento_medicine}%")).first()

    if not medicamento:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao buscar medicamento '{medicamento_medicine}', {error_msg}")
        return {"mensagem": error_msg}, 404
    else:
        logger.debug(f"Medicamento encontrado: '{medicamento.medicine}'")
        return apresenta_medicamento(medicamento), 200

@app.delete('/medicamento', tags=[medicamento_tag],
            responses={"200": MedicamentoDelSchema, "404": ErrorSchema})
def del_medicamento(query: MedicamentoBuscaSchema):
    """Deleta um Medicamento a partir do nome do medicamento informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    medicamento_medicine = unquote(unquote(query.medicine))
    print(medicamento_medicine)
    logger.debug(f"Deletando dados do medicamento #{medicamento_medicine}")

    session = Session()

    count = session.query(Medicamento).filter(Medicamento.medicine== medicamento_medicine).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado medicamento #{medicamento_medicine}")
        return {"mesage": "Medicamento removido", "id": medicamento_medicine}
    else:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao deletar medicamento #'{medicamento_medicine}', {error_msg}")
        return {"mensagem": error_msg}, 404

@app.delete('/medicamento_id', tags=[medicamento_tag],
            responses={"200": MedicamentoDelIdSchema, "404": ErrorSchema})
def del_medicamento_id(query: MedicamentoIdSchema):
    """Deleta um Medicamento a partir do id do medicamento informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    medicamento_id = query.id
    print(medicamento_id)
    logger.debug(f"Deletando dados sobre medicamento #{medicamento_id}")

    session = Session()

    count = session.query(Medicamento).filter(Medicamento.id== medicamento_id).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado medicamento #{medicamento_id}")
        return {"mensagem": "Medicamento removido", "id": medicamento_id}
    else:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao deletar medicamento #'{medicamento_id}', {error_msg}")
        return {"mensagem": error_msg}, 404
