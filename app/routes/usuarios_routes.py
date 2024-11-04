from flask import jsonify, Blueprint, request
from ..models import usuarios_models

usuarios_bp = Blueprint('usuarios', __name__)

# rota para criar conta
@usuarios_bp.route('/', methods=['POST'])
def criar_usuario_route():
    data = request.json
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    try:
        novo_usuario = usuarios_models.criar_usuario(nome, email, senha)  
        return jsonify({
                "message": "Conta criada com sucesso!",
                "usuario":{
                    "nome": novo_usuario["nome"],
                    "email": novo_usuario["email"]
                }
            }), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao criar a conta.","error": str(e)}), 500

# Rota para login
@usuarios_bp.route('/login', methods=['POST'])
def login_usuario_route():
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    try:
        usuario = usuarios_models.login_usuario(email, senha) 

        if usuario:
            return jsonify({
                "message": "Login realizado com sucesso!",
                "usuario": {
                    "id": usuario["ID_USUARIO"],
                    "nome": usuario["NOME"],
                    "email": usuario["EMAIL"],
                }
            }), 200
        else:
            return jsonify({"message": "Credenciais inválidas."}), 401
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao realizar o login.", "error": str(e)}), 500
    
# rota para obter dados do usuário pelo ID
@usuarios_bp.route('/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    try:
        # Chama a função no modelo para buscar o usuário pelo ID
        usuario = usuarios_models.get_usuario(id_usuario)
        
        if usuario:
            # Retorna os dados do usuário se encontrado
            return jsonify({
                "id": usuario["ID_USUARIO"],
                "nome": usuario["NOME"],
                "email": usuario["EMAIL"]
                
            }), 200
        else:
            # Retorna mensagem de erro se o usuário não for encontrado
            return jsonify({"message": "Usuário não encontrado."}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao buscar o usuário.", "error": str(e)}), 500

