from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Carregar os dados do arquivo JSON no início para que possam ser usados pelas rotas
with open('dados_clinica.json', 'r') as arquivo_json:
    dados_clinica = json.load(arquivo_json)

@app.route('/')
def home():
    return "Bem-vindo à API da Clínica!"

@app.route('/especialidades', methods=['GET'])
def get_especialidades():
    especialidades = [especialidade['nome'] for especialidade in dados_clinica['especialidades']]
    return jsonify(especialidades)

@app.route('/profissionais', methods=['GET'])
def get_profissionais():
    especialidade_query = request.args.get('especialidade', '').lower()
    nome_query = request.args.get('nome', '').lower()
    resultado = []

    for esp in dados_clinica['especialidades']:
        if especialidade_query and especialidade_query != esp['nome'].lower():
            continue
        for prof in esp['profissionais']:
            if nome_query and nome_query not in prof['nome'].lower():
                continue
            prof_copy = prof.copy()
            prof_copy['especialidade'] = esp['nome']
            resultado.append(prof_copy)

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
