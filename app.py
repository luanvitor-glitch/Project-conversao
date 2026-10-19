from flask import Flask, jsonify, render_template, request

from conversor import BASES, NOMES, converter

app = Flask(__name__)

# Preencha com os dados reais do grupo.
INTEGRANTES = [
    {"nome": "Integrante 1", "parte": "Lógica de conversão (conversor.py)"},
    {"nome": "Integrante 2", "parte": "Rotas Flask e validação (app.py)"},
    {"nome": "Integrante 3", "parte": "Página de conversão, modal e CSS"},
    {"nome": "Integrante 4", "parte": "Página inicial, textos e documentação"},
]

# Quais conversões cada caixa oferece. Octal é a parte EXTRA.
CAIXAS = [
    {"origem": "decimal", "destinos": ["binario", "hexadecimal", "octal"]},
    {"origem": "binario", "destinos": ["decimal", "hexadecimal", "octal"]},
    {"origem": "hexadecimal", "destinos": ["binario", "decimal", "octal"]},
    {"origem": "octal", "destinos": ["binario", "decimal", "hexadecimal"]},
]


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/grupo")
def grupo():
    return render_template("grupo.html", integrantes=INTEGRANTES)


@app.route("/conversor")
def pagina_conversor():
    return render_template("conversor.html", caixas=CAIXAS, nomes=NOMES)


@app.route("/api/converter", methods=["POST"])
def api_converter():
    dados = request.get_json(silent=True) or {}
    origem, destino = dados.get("origem"), dados.get("destino")
    valor = str(dados.get("valor", ""))
    try:
        resultado = converter(valor, origem, destino)
    except ValueError as erro:
        return jsonify(erro=str(erro)), 400
    return jsonify(resultado=resultado, entrada=valor.strip().upper(),
                   origem=NOMES[origem], destino=NOMES[destino],
                   base_origem=BASES[origem], base_destino=BASES[destino])


if __name__ == "__main__":
    app.run(debug=True)
