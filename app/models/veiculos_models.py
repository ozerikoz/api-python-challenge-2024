from flask import Blueprint
from app.db import db

usuarios_bp = Blueprint('usuarios', __name__)


# Função para adicionar um veículo ao banco de dados
def adicionar_veiculo(modelo_id, ano, cor, placa, usuario_id):
    # Nome da tabela de veículos
    t_veiculos = "t_veiculos"

    # Conexão com o banco de dados
    conn = db.get_db()

    # Cursor para executar comandos SQL
    cursor = conn.cursor()

    try:
        # Consulta SQL para inserir o veículo vinculado ao usuário
        sql_veiculo_insert = f"""
            INSERT INTO {t_veiculos} (id_modelo_veiculo, ano, cor, placa, id_usuario)
            VALUES (:id_modelo_veiculo, :ano, :cor, :placa, :id_usuario)
        """

        # Executa a inserção com os parâmetros fornecidos
        cursor.execute(sql_veiculo_insert, {
            'id_modelo_veiculo': modelo_id,
            'ano': ano,
            'cor': cor,
            'placa': placa,
            'id_usuario': usuario_id
        })
        
        conn.commit()

        return {
            "id_modelo_veiculo": modelo_id,
            "ano": ano,
            "cor": cor,
            "placa": placa,
            "usuario_id": usuario_id
        }
    except Exception as e:
        raise e
    finally:
        cursor.close()
        
# Função para remover um veículo do banco de dados com base na placa
def remover_veiculo_por_placa(id_veiculo):
    # Nome da tabela de veículos
    t_veiculos = "t_veiculos"

    # Conexão com o banco de dados
    conn = db.get_db()

    # Cursor para executar comandos SQL
    cursor = conn.cursor()

    try:
        # Verifica se o veículo com o ID existe
        sql_check_veiculo = f"SELECT 1 FROM {t_veiculos} WHERE id_veiculo = :id_veiculo"
        result = cursor.execute(sql_check_veiculo, {'id_veiculo': id_veiculo}).fetchone()

        if not result:
            return None  # Veículo não encontrado

        # Remove o veículo com o ID especificado
        sql_delete_veiculo = f"DELETE FROM {t_veiculos} WHERE id_veiculo = :id_veiculo"
        cursor.execute(sql_delete_veiculo, {'id_veiculo': id_veiculo})
        conn.commit()

        return {"id_veiculo": id_veiculo}
    except Exception as e:
        # Outros tipos de erro
        raise e
    finally:
        cursor.close()
        
# função para obter todos os fabricantes com todas as colunas
def get_fabricantes():

    t_fabricantes = "t_fabricantes"

    conn = db.get_db()
    cursor = conn.cursor()

    try:
        sql_fabricantes = f"SELECT * FROM {t_fabricantes}"
        cursor.execute(sql_fabricantes)
        resultado = cursor.fetchall()

        columns = [col[0] for col in cursor.description]

        fabricantes = []
        for row in resultado:
            fabricante = dict(zip(columns, row))
            fabricantes.append(fabricante)

        return fabricantes
    except Exception as e:
        raise e
    finally:
        cursor.close()  

# função para obter todos os fabricantes com todas as colunas
def get_modelos(id_fabricante):
    t_modelos = "t_modelos_veiculos"

    conn = db.get_db()
    cursor = conn.cursor()

    try:
        sql_modelos = f"SELECT * FROM {t_modelos} WHERE id_fabricante = :id_fabricante"
        cursor.execute(sql_modelos, {'id_fabricante': id_fabricante})
        resultado = cursor.fetchall()

        columns = [col[0] for col in cursor.description]

        modelos = []
        for row in resultado:
            modelo = dict(zip(columns, row))
            modelos.append(modelo)

        return modelos
    except Exception as e:
        raise e
    finally:
        cursor.close()
        
