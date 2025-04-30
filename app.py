from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Caminho para o arquivo db.json
DB_FILE = 'db.json'

def read_db():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"mensagens": []}

def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/mensagens', methods=['POST'])
def criar_mensagem():
    db = read_db()
    nova_mensagem = {
        'id': str(len(db['mensagens']) + 1),
        'conteudo': request.json.get('conteudo', '')
    }
    db['mensagens'].append(nova_mensagem)
    write_db(db)
    return jsonify(nova_mensagem), 201

@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    db = read_db()
    return jsonify(db['mensagens'])

@app.route('/mensagens/<id>', methods=['GET'])
def obter_mensagem(id):
    db = read_db()
    mensagem = next((m for m in db['mensagens'] if m['id'] == id), None)
    if mensagem:
        return jsonify(mensagem)
    return jsonify({"error": "Mensagem não encontrada"}), 404

@app.route('/mensagens/<id>', methods=['PUT'])
def atualizar_mensagem(id):
    db = read_db()
    for mensagem in db['mensagens']:
        if mensagem['id'] == id:
            mensagem['conteudo'] = request.json.get('conteudo', mensagem.get('conteudo', ''))
            write_db(db)
            return jsonify(mensagem)
    return jsonify({"error": "Mensagem não encontrada"}), 404

@app.route('/mensagens/<id>', methods=['DELETE'])
def deletar_mensagem(id):
    db = read_db()
    for i, mensagem in enumerate(db['mensagens']):
        if mensagem['id'] == id:
            deletada = db['mensagens'].pop(i)
            write_db(db)
            return jsonify(deletada)
    return jsonify({"error": "Mensagem não encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)