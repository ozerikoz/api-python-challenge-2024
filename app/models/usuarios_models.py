from flask import Blueprint
from app.db import db

usuarios_bp = Blueprint('usuarios', __name__)

# função para criar um usuário
def criar_usuario(nome, email, senha):
    # Nome da tabela de usuários
    t_usuarios = "t_usuarios"

    # Conexão com o banco de dados
    conn = db.get_db()

    # Cursor para executar comandos SQL
    cursor = conn.cursor()
    
    try:
        # verifica se o usuário já existe usando SQL direto
        sql_usuario_check = f"SELECT 1 FROM {t_usuarios} WHERE email = :email"
        result = cursor.execute(sql_usuario_check, {'email': email}).fetchone()

        if result:
            raise ValueError("Usuário com esse email já existe!")

        # insere o novo usuário no banco de dados
        sql_usuario_insert = f"INSERT INTO {t_usuarios} (nome, email, senha) VALUES (:nome, :email, :senha)"
        cursor.execute(sql_usuario_insert, {'nome': nome, 'email': email, 'senha': senha})
        conn.commit()

        return {"nome": nome, "email": email}
    except Exception as e:
        raise e
    finally:
        cursor.close()
        
# Função para validar o login do usuário
def login_usuario(email, senha):
    # Nome da tabela de usuários
    t_usuarios = "t_usuarios"

    # Conexão com o banco de dados
    conn = db.get_db()

    # Cursor para executar comandos SQL
    cursor = conn.cursor()
    
    try:
        # Verifica se o usuário existe e a senha está correta
        sql_usuario_login = f"SELECT * FROM {t_usuarios} WHERE email = :email AND senha = :senha"
        result = cursor.execute(sql_usuario_login, {'email': email, 'senha': senha}).fetchone()

        if result:
            columns = [col[0] for col in cursor.description]
            usuario = dict(zip(columns, result)) 
            return usuario  # Retorna o dicionário com todos os dados do usuário
        else:
            return None  # Retorna None se as credenciais estiverem incorretas
    except Exception as e:
        raise e
    finally:
        cursor.close()

# função para obter os dados do usuario 
def get_usuario(id_usuario):
    # Nome da tabela de usuários
    t_usuarios = "t_usuarios"

    # Conexão com o banco de dados
    conn = db.get_db()
    cursor = conn.cursor()

    try:
        # Consulta SQL para buscar o usuário pelo ID
        sql_usuario = f"SELECT * FROM {t_usuarios} WHERE ID_USUARIO = :id_usuario"
        result = cursor.execute(sql_usuario, {'id_usuario': id_usuario}).fetchone()

        if result:
            # Constrói um dicionário com todos os dados do usuário
            columns = [col[0] for col in cursor.description]
            usuario = dict(zip(columns, result))
            return usuario
        else:
            return None
    except Exception as e:
        raise e
    finally:
        cursor.close()

