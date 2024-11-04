from flask import Blueprint, jsonify, request
from ..models import veiculos_models

veiculos_bp = Blueprint('veiculos', __name__)

# rota para adicionar veículo
@veiculos_bp.route('/', methods=['POST'])
def adicionar_veiculo_route():
    data = request.json
    modelo_id = data.get("id_modelo_veiculo")
    ano = data.get("ano")
    cor = data.get("cor")
    placa = data.get("placa")
    usuario_id = data.get("id_usuario")

    # Verifica se todos os campos obrigatórios estão preenchidos
    if not all([modelo_id, ano, cor, placa, usuario_id]):
        return jsonify({"message": "Todos os campos (id_modelo_veiculo, ano, cor, placa, id_usuario) são obrigatórios."}), 400
    
    try:
        veiculo = veiculos_models.adicionar_veiculo(modelo_id, ano, cor, placa, usuario_id)
        return jsonify({
            "message": "Veículo adicionado com sucesso!",
            "veiculo": veiculo
        }), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao adicionar o veículo.", "error": str(e)}), 500


# rota para remover veículo por placa
@veiculos_bp.route('/<int:id_veiculo>', methods=['DELETE'])
def remover_veiculo_route(id_veiculo):
    try:
        veiculo = veiculos_models.remover_veiculo_por_placa(id_veiculo)
        
        if veiculo:
            return jsonify({
                "message": "Veículo removido com sucesso!",
            }), 200
        else:
            return jsonify({"message": "Veículo não encontrado."}), 404
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao remover o veículo.", "error": str(e)}), 500

# rota para obter todos os fabricantes com seleção de campos
@veiculos_bp.route('/fabricantes', methods=['GET'])
def get_fabricantes_route():
    try:
        fabricantes_completos = veiculos_models.get_fabricantes()

        fabricantes_resumidos = [
            {
                "id_fabricante": fabricante["ID_FABRICANTE"],
                "nome": fabricante["NOME"]
            }
            for fabricante in fabricantes_completos
        ]

        return jsonify({
            "fabricantes": fabricantes_resumidos
        }), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao buscar os fabricantes.", "error": str(e)}), 500

# rota para obter todos os fabricantes com seleção de campos
@veiculos_bp.route('/modelos/<int:id_fabricante>', methods=['GET'])
def get_modelos_route(id_fabricante):
    try:
        fabricantes_completos = veiculos_models.get_modelos(id_fabricante)

        fabricantes_resumidos = [
            {
                "id_fabricante": fabricante["ID_FABRICANTE"],
                "id_modelo": fabricante["ID_MODELO_VEICULO"],
                "nome": fabricante["NOME"]
            }
            for fabricante in fabricantes_completos
        ]

        return jsonify({
            "fabricantes": fabricantes_resumidos
        }), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Ocorreu um erro ao buscar os fabricantes.", "error": str(e)}), 500
